from app import app
from flask import render_template, url_for, redirect, jsonify, flash
from app.competition.forms import CompetitionInsertForm, CompetitionUpdateForm, CompetitionDeleteForm
from werkzeug.http import HTTP_STATUS_CODES
from func_pack import get_api_info, get_current_datetime, str_to_right_type,\
    get_account_info_by_account_id
from config import Config
from app.competition import bp
from flask_login import current_user, login_required
import requests
import datetime


# ------------ Competition Routing -------------- #
# competition inserting
@login_required
@bp.route('/competition-inserting', methods=['GET'])
def competition_inserting_view():
    form = CompetitionInsertForm()
    return render_template('competition/compInsert.html', form=form)


# competition inserting function
@login_required
@bp.route('/competition-inserting', methods=['POST'])
def competition_inserting_function():
    # auth process
    if current_user.is_authenticated is True:
        account = get_account_info_by_account_id(current_user.account_id)
    else:
        return redirect(url_for('auth.login_view'))
    # process end

    form = CompetitionInsertForm()
    if form.validate_on_submit():
        insert_url = 'http://' + Config.COMPETITION_SERVICE_URL + \
            '/api/competition'
        new_competition = dict()

        new_competition['comp_title'] = form.comp_title.data
        new_competition['comp_subtitle'] = form.comp_subtitle.data
        new_competition['comp_range'] = form.comp_range.data
        new_competition['comp_url'] = form.comp_url.data
        new_competition['prize_currency'] = form.prize_currency.data
        new_competition['prize_amount'] = form.prize_amount.data
        new_competition['deadline'] = form.deadline.data
        new_competition['timezone'] = form.timezone.data
        new_competition['update_time'] = get_current_datetime()
        new_competition['publish_time'] = get_current_datetime()
        new_competition['contributor_id'] = str(current_user.account_id)
        new_competition['contributor_name'] = str(account['account_nickname'])

        new_competition['comp_description'] = form.comp_description.data
        host_list = [{'comp_host_name': form.comp_host_name.data, 'comp_host_url': form.comp_host_url.data}]
        new_competition['comp_host'] = str(host_list)

        comp_scenario_list = str_to_right_type(str(form.comp_scenario.data))
        new_competition['comp_scenario'] = str(comp_scenario_list)
        data_feature = str_to_right_type(str(form.data_feature.data))
        new_competition['data_feature'] = str(data_feature)

        result = requests.post(insert_url, data=new_competition)
        if result.status_code == 200:
            competition = get_api_info(result)[0]
            comp_record_hash = competition['comp_record_hash']
            return redirect(url_for('competition-operator.competition_detail_view', comp_record_hash=comp_record_hash))
        else:
            flash('Something wrong happened! Can not upload competition', 'danger')
            return redirect(url_for('competition-operator.competition_inserting_view'))


# my competition list
@login_required
@bp.route('/competition-list/<string:user_id>', methods=['GET'])
def competition_list_view(user_id):
    # check user's authentication by account_id in url whether match current_user.account_id
    # Mention!! Type of current_user.account_id is not string!
    if str(current_user.account_id) != user_id:
        auth = {'operator': False}
    else:
        auth = {'operator': True}

    # account function
    account_url = 'http://' + Config.ACCOUNT_SERVICE_URL + \
                  '/api/account/account-id/' + str(user_id)
    result = requests.get(account_url)
    if result.status_code == 200 and len(get_api_info(result)) > 0:
        auth['account_nickname'] = get_api_info(result)[0]['account_nickname']
    else:
        auth['account_nickname'] = 'Unknown'

    # main function process below
    own_competition_url = 'http://' + Config.COMPETITION_SERVICE_URL + \
                          '/api/competition/contributor-id/' + str(user_id)
    result = requests.get(own_competition_url)
    if result.status_code == 200:
        owner_comps_list = get_api_info(result)
        owner_comps_list.reverse()
        return render_template('competition/compMenu.html', comp_list=owner_comps_list, auth=auth)


# competition detail view
@bp.route('/competition-detail/<string:comp_record_hash>', methods=['GET'])
def competition_detail_view(comp_record_hash):
    comp_url = 'http://' + Config.COMPETITION_SERVICE_URL + \
               '/api/competition/competition-record-hash/' + str(comp_record_hash)
    type_dict =    {"DM": "Data Mining",
                    "CV" : "Computer Vision",
                    "NLP": "Natural Language Processing",
                    "RL": "Reinforcement Learning/Robotics",
                    "SP": "Speech/Signal Proccessing"}               
    result = requests.get(comp_url)
    if result.status_code == 200:
        competition = get_api_info(result)[0]
        # check user's authentication by account_id in url whether match current_user.account_id
        # Mention!! Type of current_user.account_id is not string!
        if str(current_user.account_id) != competition['contributor_id']:
            auth = {'operator': False}
        else:
            auth = {'operator': True}
        return render_template('competition/compView.html', competition=competition, auth=auth,
                               type_dict=type_dict)


# competition update page
@bp.route('/competition-updating/<string:comp_record_hash>', methods=['GET'])
@login_required
def competition_updating_view(comp_record_hash):
    comp_url = 'http://' + Config.COMPETITION_SERVICE_URL + \
               '/api/competition/competition-record-hash/' + str(comp_record_hash)
    result = requests.get(comp_url)
    if result.status_code == 200 and len(get_api_info(result)) >= 1:
        competition = get_api_info(result)[0]
        # check user's authentication by account_id in url whether match current_user.account_id
        # Mention!! Type of current_user.account_id is not string!
        if str(current_user.account_id) != str(competition['contributor_id']):
            # back to detail viewing page
            return redirect(url_for('competition-operator.competition_detail_view', comp_record_hash=comp_record_hash))

        # main function process below
        form = CompetitionUpdateForm()
        form.comp_title.data = competition['comp_title']
        form.comp_subtitle.data = competition['comp_subtitle']
        form.comp_range.data = competition['comp_range']
        form.comp_url.data = competition['comp_url']
        form.comp_description.data = competition['comp_description']
        form.comp_host_name.data = competition['comp_host'][0]['comp_host_name']
        form.comp_host_url.data = competition['comp_host'][0]['comp_host_url']
        form.prize_currency.data = competition['prize_currency']
        form.prize_amount.data = competition['prize_amount']
        form.deadline.data = datetime.datetime.strptime(competition['deadline'], '%Y-%m-%d %H:%M:%S')
        form.timezone.data = competition['timezone']
        comp_scenario = list()
        for scenario in competition['comp_scenario']:
            comp_scenario.append(scenario)
        form.comp_scenario.data = comp_scenario
        data_feature = list()
        for feature in competition['data_feature']:
            data_feature.append(feature)        
        form.data_feature.data = data_feature
        return render_template('competition/compUpdate.html', form=form)


# competition update post
@bp.route('/competition-updating/<string:comp_record_hash>', methods=['POST'])
@login_required
def competition_updating_function(comp_record_hash):
    form = CompetitionUpdateForm()
    if form.validate_on_submit():
        # Get competition info
        comp_url = 'http://' + Config.COMPETITION_SERVICE_URL + \
                   '/api/competition/competition-record-hash/' + str(comp_record_hash)
        result = requests.get(comp_url)
        if result.status_code == 200:
            mod_competition = get_api_info(result)[0]

            # check user's authentication by account_id in url whether match current_user.account_id
            # Mention!! Type of current_user.account_id is not string!
            if str(current_user.account_id) != str(mod_competition['contributor_id']):
                # back to detail viewing page
                return redirect(
                    url_for('competition-operator.competition_detail_view', comp_record_hash=comp_record_hash))

            # Update Info
            update_url = 'http://' + Config.COMPETITION_SERVICE_URL + \
                '/api/competition/competition-record-hash/' + comp_record_hash

            mod_competition['comp_title'] = form.comp_title.data
            mod_competition['comp_subtitle'] = form.comp_subtitle.data
            mod_competition['comp_range'] = form.comp_range.data
            mod_competition['comp_url'] = form.comp_url.data
            mod_competition['prize_currency'] = form.prize_currency.data
            mod_competition['prize_amount'] = form.prize_amount.data
            mod_competition['deadline'] = form.deadline.data
            mod_competition['timezone'] = form.timezone.data
            mod_competition['update_time'] = get_current_datetime()

            mod_competition['comp_description'] = form.comp_description.data
            host_list = [{'comp_host_name': form.comp_host_name.data, 'comp_host_url': form.comp_host_url.data}]
            mod_competition['comp_host'] = str(host_list)

            comp_scenario_list = str_to_right_type(str(form.comp_scenario.data))
            mod_competition['comp_scenario'] = str(comp_scenario_list)
            data_feature = str_to_right_type(str(form.data_feature.data))
            mod_competition['data_feature'] = str(data_feature)

            result = requests.put(update_url, data=mod_competition)
            if result.status_code == 200:
                user_id = get_api_info(result)[0]['contributor_id']
                return redirect(url_for('competition-operator.competition_detail_view',
                                        comp_record_hash=mod_competition['comp_record_hash']))


# competition delete view
@bp.route('/competition-deleting/<string:comp_record_hash>', methods=['GET', 'POST'])
@login_required
def competition_delete_confirm(comp_record_hash):
    form = CompetitionDeleteForm()
    # Get competition info
    comp_url = 'http://' + Config.COMPETITION_SERVICE_URL + \
               '/api/competition/competition-record-hash/' + str(comp_record_hash)
    result = requests.get(comp_url)
    # Functional Part
    if form.validate_on_submit():
        if result.status_code == 200:
            user_id = get_api_info(result)[0]['contributor_id']

            # check user's authentication by account_id in url whether match current_user.account_id
            # Mention!! Type of current_user.account_id is not string!
            if str(current_user.account_id) != str(user_id):
                # back to detail viewing page
                return redirect(
                    url_for('competition-operator.competition_detail_view', comp_record_hash=comp_record_hash))

            # main function process below
            delete_url = 'http://' + Config.COMPETITION_SERVICE_URL + \
                         '/api/competition/competition-record-hash/' + str(comp_record_hash)
            requests.delete(delete_url)
            return redirect(url_for('competition-operator.competition_list_view', user_id=user_id))
    # View Part
    else:
        if result.status_code == 200:
            user_id = get_api_info(result)[0]['contributor_id']

            # check user's authentication by account_id in url whether match current_user.account_id
            # Mention!! Type of current_user.account_id is not string!
            if str(current_user.account_id) != str(user_id):
                # back to detail viewing page
                return redirect(
                    url_for('competition-operator.competition_detail_view', comp_record_hash=comp_record_hash))

            # main function process below
            competition = get_api_info(result)[0]
            return render_template('competition/compDelete.html', form=form, competition=competition)


# # competition delete function
# @bp.route('/competition-deleting/<string:comp_record_hash>', methods=['DELETE'])
# def competition_deleting_function(comp_record_hash):
#     comp_url = 'http://' + Config.COMPETITION_SERVICE_URL + \
#                '/api/competition/competition-record-hash/' + str(comp_record_hash)
#     result = requests.get(comp_url)
#     if result.status_code == 200:
#         user_id = get_api_info(result)[0]
#         delete_url = 'http://' + Config.COMPETITION_SERVICE_URL + \
#             '/api/competition/competition-record-hash/' + str(comp_record_hash)
#         result = requests.delete(delete_url)
#         if result == 200:
#             return redirect(url_for('competition-operator.competition_list_view', user_id=user_id))


# bad requests holder
def bad_request(message):
    return error_response(400, message)


# error response
def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response

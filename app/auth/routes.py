from app import app
from flask import render_template, url_for, redirect, flash, request, session
from app.auth.forms import ResetPasswordRequestForm, ResetPasswordForm, RegisterRequestForm, LoginForm, RegisterForm
from func_pack import get_api_info, generate_random_code
from config import Config
from app.auth import bp
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User
import requests


# ------------ Auth routing -------------- #
# reset password request template
@bp.route('/reset-password-request', methods=['GET'])
def reset_password_request():
    form = ResetPasswordRequestForm()
    return render_template('auth/email/reset_password_request.html', form=form)


# reset password request Post
@bp.route('/reset-password-request', methods=['POST'])
def reset_password_request_receive_form():
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        account_email = form.email.data
        dest_url = 'http://' + Config.MAIL_SENDING_SERVICE_URL + '/api/reset-password/email-sending-by-account-email'
        result = requests.post(dest_url, data={'account_email': account_email})
        account_to_reset = get_api_info(result)
        return render_template('auth/email/inform_reset_email.html', account_email=account_email)


# receiving password token
@bp.route('/reset-password/<string:token>', methods=['GET'])
def reset_password_receiving_token(token):
    form = ResetPasswordForm()
    dest_url = 'http://' + Config.MAIL_SENDING_SERVICE_URL + '/api/reset-password/token-receiving/' +\
               str(token)
    result = requests.get(dest_url)
    if result.status_code == 200:
        account_to_reset = get_api_info(result)[0]
        return render_template('auth/email/reset_password.html', form=form, account_email=account_to_reset['account_email'])


# reset password
@bp.route('/reset-password/<string:token>', methods=['POST'])
def reset_password(token):
    form = ResetPasswordForm()
    if form.validate_on_submit():
        dest_url = 'http://' + Config.MAIL_SENDING_SERVICE_URL + '/api/reset-password/token-receiving/' +\
                   str(token)
        new_password = str(form.re_new_password.data)
        result = requests.get(dest_url)
        account_to_reset = get_api_info(result)[0]
        account_to_reset['password'] = new_password
        update_account_url = 'http://' + Config.ACCOUNT_SERVICE_URL + '/api/account/account-updating'
        requests.put(update_account_url, data=account_to_reset)
        return render_template('auth/email/inform_reset_success.html', form=form, account_email=account_to_reset['account_email'])


# register confirmation
@bp.route('/register-confirmation/<string:token>', methods=['GET'])
@login_required
def register_confirmation(token):
    dest_url = 'http://' + Config.MAIL_SENDING_SERVICE_URL + '/api/registration/token-receiving/' +\
               token
    result = requests.get(dest_url)
    if result.status_code == 200:
        return render_template('auth/email/register_confirmation.html')


# -------------- Login View --------------- #
# Login View
@bp.route('/login', methods=['GET'])
def login_view():
    # check whether user has already login
    if current_user.is_authenticated:
        return redirect(url_for('auth.home_view', account_id=current_user.account_id))

    # main function process below
    form = LoginForm()
    captcha = dict()
    captcha_url = 'http://' + Config.CAPTCHA_SERVICE_URL + '/api/hash-match/captcha'
    result = requests.get(captcha_url)
    if result.status_code == 200:
        captcha['captcha_code'] = get_api_info(result)[0]['CAPTCHA']
        captcha['hash_code'] = get_api_info(result)[0]['Hash-Code']
        # store the captcha code into session
        session['captcha_code'] = captcha['captcha_code']
        captcha['captcha_url'] = 'http://' + Config.CAPTCHA_SERVICE_URL +\
                                 '/api/hash-match/captcha/' + captcha['hash_code']
    else:
        captcha['captcha_code'] = '0000'
        captcha['captcha_url'] = 'error'
    return render_template('auth/login/login.html', form=form, captcha=captcha)


# Login verify
@bp.route('/login', methods=['POST'])
def login_verify():
    # check whether user has already login
    if current_user.is_authenticated:
        return redirect(url_for('auth.home_view', account_id=current_user.account_id))

    # main function process below
    form = LoginForm()
    if form.validate_on_submit():
        # POST method
        if form.validate_on_submit():
            # captcha validate ( get from session )
            if str(form.captcha.data).upper() != session.get('captcha_code'):
                flash('CAPTCHA is not Correct!', 'warning')
                return redirect(url_for('auth.login_view'))
        account_email = form.email.data
        password = form.password.data
        dest_url = 'http://' + Config.ACCOUNT_SERVICE_URL + '/api/account/validate-password'
        result = requests.post(dest_url, data={'account_email': account_email, 'password': password})
        if result.status_code == 200 and len(get_api_info(result)) > 0:
            account = get_api_info(result)[0]
            if account['account_id'] != -1:
                # add auth
                verified_user = User(account_id=account['account_id'])
                login_user(verified_user)
                return redirect(url_for('auth.home_view', account_id=account['account_id']))
            else:
                flash('Email unknown or Password is not correct.', 'danger')
                return redirect(url_for('auth.login_view'))


# -------------- Register View --------------- #
# register view
@bp.route('/register', methods=['GET'])
def register_view():
    # check whether user has already login
    if current_user.is_authenticated:
        return redirect(url_for('auth.home_view', account_id=current_user.account_id))

    # main function process below
    form = RegisterForm()
    captcha = dict()
    captcha_url = 'http://' + Config.CAPTCHA_SERVICE_URL + '/api/hash-match/captcha'
    result = requests.get(captcha_url)
    if result.status_code == 200:
        captcha['captcha_code'] = get_api_info(result)[0]['CAPTCHA']
        captcha['hash_code'] = get_api_info(result)[0]['Hash-Code']
        # store the captcha code into session
        session['captcha_code'] = captcha['captcha_code']
        captcha['captcha_url'] = 'http://' + Config.CAPTCHA_SERVICE_URL +\
                                 '/api/hash-match/captcha/' + captcha['hash_code']
    else:
        captcha['captcha_code'] = '0000'
        captcha['captcha_url'] = 'error'
    return render_template('auth/register/register.html', form=form, captcha=captcha)


# register post
@bp.route('/register', methods=['POST'])
def register_account():
    # check whether user has already login
    if current_user.is_authenticated:
        return redirect(url_for('auth.home_view', account_id=current_user.account_id))

    # main function process below
    form = RegisterForm()
    # POST method
    if form.validate_on_submit():
        # captcha validate ( get from session )
        if str(form.captcha.data).upper() != session.get('captcha_code'):
            flash('CAPTCHA is not Correct!', 'warning')
            return redirect(url_for('auth.register_view'))
        if form.password.data != form.re_password.data:
            flash('Passwords should be the same.', 'warning')
            return redirect(url_for('auth.register_view'))
        # account info
        account_info = dict()
        account_info['account_email'] = form.email.data
        account_info['account_nickname'] = form.nickname.data
        account_info['password'] = form.re_password.data
        register_url = 'http://' + Config.ACCOUNT_SERVICE_URL + '/api/account/account-creating'
        result = requests.post(register_url, data=account_info)
        if result.status_code == 200:
            account = get_api_info(result)[0]
            return redirect(url_for('auth.login_view', account_id=account['account_id']))
        else:
            flash('Please use an different email address.', 'danger')
            return redirect(url_for('auth.register_view'))


# ---------------- Home Page ---------------- #
# home page
@bp.route('/home/<string:account_id>', methods=['GET'])
@login_required
def home_view(account_id):
    # check user's authentication by account_id in url whether match current_user.account_id
    # Mention!! Type of current_user.account_id is not string!
    if str(current_user.account_id) != account_id:
        return redirect(url_for('auth.home_view', account_id=str(current_user.account_id)))

    # main function process below
    form = RegisterRequestForm()
    account_info_url = 'http://' + Config.ACCOUNT_SERVICE_URL + '/api/account/account-id/' +\
        str(account_id)
    result = requests.get(account_info_url)
    if result.status_code == 200:
        account_info = get_api_info(result)[0]
        return render_template('auth/individual/home_page.html', form=form, account=account_info)
    else:
        return redirect(url_for('auth.login_view'))


# sending registration email
@bp.route('/home/<string:account_id>', methods=['POST'])
@login_required
def home_post(account_id):
    # check user's authentication by account_id in url whether match current_user.account_id
    # Mention!! Type of current_user.account_id is not string!
    if str(current_user.account_id) != account_id:
        return redirect(url_for('auth.home_view', account_id=str(current_user.account_id)))

    # main function process below
    form_register_request = RegisterRequestForm()
    if form_register_request.validate_on_submit():
        account_info_url = 'http://' + Config.ACCOUNT_SERVICE_URL + '/api/account/account-id/' + \
                           str(account_id)
        result = requests.get(account_info_url)
        if result.status_code == 200:
            account_info = get_api_info(result)[0]
            print(account_info)
            dest_url = 'http://' + Config.MAIL_SENDING_SERVICE_URL + '/api/registration/email-sending-by-account-email'
            result = requests.post(dest_url, data={'account_email': account_info['account_email']})
            if result.status_code == 200:
                return render_template('auth/email/inform_register_email.html')



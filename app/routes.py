from app import app
from flask import render_template, request, redirect, url_for, Response
from config import Config
from func_pack import get_api_info
from flask_login import logout_user
from app.models import User
import requests
import datetime
import numpy as np
# import pytz, heapq # 堆队列


# id_type_checkboxs = [
#     {"id": "PF-checkbox", "name": "Platform"}
#     # ,{'id': 'IT-checkbox', 'name': 'Industry'}
#     ,
#     {"id": "AC-checkbox", "name": "Academia"},
# ]

id_type2_checkboxs = [
    {"id": "DM-checkbox", "name": "Data Mining"},
    {"id": "CV-checkbox", "name": "Computer Vision"},
    {"id": "NLP-checkbox", "name": "Natural Language Processing"},
    {"id": "RL-checkbox", "name": "Reinforcement Learning/Robotics"},
    {"id": "SP-checkbox", "name": "Speech/Signal Proccessing"},
]

type_dict = {
    "DM": "Data Mining","CV": "Computer Vision",
    "NLP": "Natural Language Processing",
    "RL": "Reinforcement Learning/Robotics",
    "SP": "Speech/Signal Proccessing"}

Func_deadline = lambda x: x['deadline']
# 严格要求 deadline 的格式：%Y-%m-%d %H:%M:%S
Filtering_pastcomp = lambda comps: [ comp for comp in comps if nonFiltering_deadline(comp)]
Filtering_hashcomp = lambda comps, hash: [ comp for comp in comps if comp['comp_record_hash'] == hash]

def nonFiltering_deadline(comp):
    if comp['deadline']:
        # print(type(comp['deadline']), comp['deadline'])
        return int(''.join(comp['deadline'].split()[0].split('-')))>=int(datetime.datetime.today().strftime('%Y%m%d'))
    else:
        comp['deadline'] = 'No deadline'  # Working for empty in comp['deadline']
        return True
    

@app.route("/")
@app.route("/index")
def index():
    addr = 'http://' + Config.COMPETITION_SERVICE_URL + '/api/competition/all-competitions'
    info_list = get_api_info(requests.get(addr))
    info_list = sorted(Filtering_pastcomp(info_list), key=Func_deadline) # Filtering and sort the list by deadline

    return render_template(
        "index.html",
        # id_type_checkboxs=id_type_checkboxs,
        id_type2_checkboxs=id_type2_checkboxs,
        competitions=info_list,
    )


# -------------- Log Out --------------- #
@app.route('/logout', methods=['GET'])
def logout_func():
    logout_user()
    return redirect(url_for('auth.login_view'))


# Founders of the website
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


# XML

@app.route("/update_log.xml")
def products_xml():

    addr = 'http://' + Config.COMPETITION_SERVICE_URL + '/api/competition/all-competitions'
    info_list = get_api_info(requests.get(addr))
    competitions = sorted(Filtering_pastcomp(info_list), key=Func_deadline) # Filtering and sort the list by deadline


    # num_largest = 2
    # comps_pubtime = np.array([int(i["pubtime"].replace("-", "")) for i in competitions])
    # comps_pubtime = np.array([int(comp['publish_time'][:10].replace("-", "")) for comp in competitions])
    comps_pubtime = np.array([comp['publish_time'] for comp in competitions])
    valid_index = [datetime.datetime.strptime(pubtime, '%Y-%m-%d %H:%M:%S') >= (datetime.datetime.today()-datetime.timedelta(days=7)) for pubtime in comps_pubtime]
    competitions = np.array(competitions)[np.array(valid_index)] #  Filtering the comps for a week



    # time_largest = heapq.nlargest(num_largest, np.unique(comps_pubtime))
    # index_largest = [
    #     np.where(comps_pubtime == largest_value)[0].tolist()
    #     for largest_value in time_largest
    # ]
    # competitions = [
    #     (competitions[largest_index], block_time)
    #     for block_time, largest_time in enumerate(index_largest)
    #     for largest_index in largest_time
    # ]

    # [
    #     comp.update(
    #         {
    #             "pubtime": datetime.datetime.fromtimestamp(
    #                 int(
    #                     datetime.datetime.strptime(
    #                         comp["pubtime"], "%Y-%m-%d"
    #                     ).timestamp()
    #                 ),
    #                 pytz.timezone("Asia/Shanghai"),
    #             ).strftime("%a, %d %b %Y")
    #         }
    #     )
    #     for comp, _ in competitions
    # ]

    output = '<?xml version="1.0" encoding="UTF-8" ?>'
    output += '<rss version="2.0">'
    output += "<channel>"
    output += "<title>DataSciCamp: Data Science Challenge / Competition</title>"
    output += "<link>https://www.datascicamp.com/</link>"
    output += "<description>Update within the last 7 days!</description>"
    # update_block = [
    #     datetime.datetime.fromtimestamp(
    #         int(
    #             datetime.datetime.strptime(
    #                 str(time_largest[block]), "%Y%m%d"
    #             ).timestamp()
    #         ),
    #         pytz.timezone("Asia/Shanghai"),
    #     ).strftime("%m/%d/%Y")
    #     for block in range(num_largest)
    # ]
    # output += "<description>Latest update at {} (GMT+0800).</description>".format(
    #     update_block[0]
    # )

    for comp in competitions:
        output += "<item>"
        output += "<title>{:s}</title>".format(comp["comp_title"])
        output += "<link>{:s}</link>".format("https://www.datascicamp.com/competition-operator/competition-detail/"+comp["comp_record_hash"])
        # output += "<category>{:s}</category>".format("/".join(comp["type1"]))
        output += "<category>{:s}</category>".format("/".join(comp["comp_scenario"]))
        output += "<pubDate>{:s}</pubDate>".format(comp["publish_time"])
        output += "<description>{:s}</description>".format(
            comp["comp_description"].replace("<br>", "")
        )
        output += "</item>"
    output += "</channel>"
    output += "</rss>"
    return Response(output, mimetype="application/xml")
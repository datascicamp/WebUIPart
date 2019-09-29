from app import app
from flask import render_template, request, redirect, url_for
from config import Config
from func_pack import get_api_info
from flask_login import logout_user
from app.models import User
import requests
import datetime


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

type_dict =    {"DM": "Data Mining",
                "CV" : "Computer Vision",
                "NLP": "Natural Language Processing",
                "RL": "Reinforcement Learning/Robotics",
                "SP": "Speech/Signal Proccessing"}

Func_deadline = lambda x: x['deadline']
# 严格要求 deadline 的格式：%Y-%m-%d %H:%M:%S
Filtering_pastcomp = lambda comps: [ comp for comp in comps if int(''.join(comp['deadline'].split()[0].split('-')))>=int(datetime.datetime.today().strftime('%Y%m%d'))]
Filtering_hashcomp = lambda comps, hash: [ comp for comp in comps if comp['comp_record_hash'] == hash]


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

# @app.route("/competition=<comp_record_hash>", )
# def comp(comp_record_hash):
#     addr = 'http://' + Config.COMPETITION_SERVICE_URL + '/api/competition/all-competitions'
#     info_list = get_api_info(requests.get(addr))
#     info_list = Filtering_hashcomp(info_list, comp_record_hash) # Filtering the list by comp_record_hash
#     assert len(info_list) == 1
#     print(info_list)
#     return render_template(
#         "competition.html",
#         Comp=info_list[0],
#         type_dict=type_dict,
#     )

# @app.route("/hostby.html")
# def hostby(id_type_checkboxs=id_type_checkboxs, hosts=hosts):
#     return render_template(
#         "hostby.html", id_type_checkboxs=id_type_checkboxs, hosts=hosts
#     )

from app import app
from flask import render_template, request, redirect, url_for
from config import Config
from func_pack import get_api_info
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User
import requests


id_type_checkboxs = [
    {"id": "PF-checkbox", "name": "Platform"}
    # ,{'id': 'IT-checkbox', 'name': 'Industry'}
    ,
    {"id": "AC-checkbox", "name": "Academia"},
]

id_type2_checkboxs = [
    {"id": "DM-checkbox", "name": "Data Mining"},
    {"id": "CV-checkbox", "name": "Computer Vision"},
    {"id": "NLP-checkbox", "name": "Natural Language Processing"},
    {"id": "RL-checkbox", "name": "Reinforcement Learning/Robotics"},
    {"id": "SP-checkbox", "name": "Speech/Signal Proccessing"},
]


@app.route('/')
@app.route('/index')
def index():
    addr = Config.ADDRESS_COMP
    info_list = get_api_info(requests.get(addr))
    return render_template('index.html', 
        id_type_checkboxs=id_type_checkboxs,
    id_type2_checkboxs=id_type2_checkboxs,
    competitions = info_list)

# @app.route("/hostby.html")
# def hostby(id_type_checkboxs=id_type_checkboxs, hosts=hosts):
#     return render_template(
#         "hostby.html", id_type_checkboxs=id_type_checkboxs, hosts=hosts
#     )

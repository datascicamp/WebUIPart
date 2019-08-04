from app import app
from flask import render_template, request, redirect, url_for
from config import Config
from func_pack import get_api_info
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User
import requests


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


from flask import Blueprint

bp = Blueprint('competition-operator', __name__)

from app.competition import routes


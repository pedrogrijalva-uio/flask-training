from flask import Blueprint

login = Blueprint('auth', __name__)

from . import views

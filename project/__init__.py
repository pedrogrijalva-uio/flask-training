import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from instance import config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config.Config)
Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from flask_login import LoginManager
from .models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(email):
    return User.query.filter_by(email= email).first()


from .profile import profile as profile_blueprint
from .registration import registration as registration_blueprint
from .login import login as login_blueprint

app.register_blueprint(profile_blueprint, url_prefix='/profile')
app.register_blueprint(registration_blueprint)
app.register_blueprint(login_blueprint)

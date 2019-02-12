import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from instance import config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config.Config)
Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect()
csrf.init_app(app)
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from flask_login import LoginManager
from .models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.loginuser"
# login_manager.session_protection = "strong"
# login_manager.refresh_view = "auth.loginuser"


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


from .profile import profile as profile_blueprint
from .registration import registration as registration_blueprint
from .auth import login as login_blueprint

app.register_blueprint(profile_blueprint, url_prefix='/profile')
app.register_blueprint(registration_blueprint)
app.register_blueprint(login_blueprint)

import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

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

from project import models

from .profile import profile as profile_blueprint
from .registration import registration as registration_blueprint

app.register_blueprint(profile_blueprint, url_prefix='/profile')
app.register_blueprint(registration_blueprint)


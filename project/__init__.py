import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from instance import config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from .models import User

@app.route('/hello')
def hello():
    User.create(name='nombre',email='nombre@test.com',passwd='test2')
    return 'Hello, World!'


@app.route('/')
def home():
    return 'PGrijalva Training!'

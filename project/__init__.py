import os
import instance.config
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    print(test_config)
    if test_config is None:
        app.config.from_pyfile('flask.cfg', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    def home():
        return 'PGrijalva Training!'
    
    return app

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or '3b1ae534-eedf-4c58-baf2-ae87bef78836'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:docker@0.0.0.0/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False
    WTF_CSRF_METHODS = ['POST', 'PUT', 'PATCH']


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class TestConfig(Config):
    TEST = True

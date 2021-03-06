import os
from unittest.mock import MagicMock

import pytest

from project import app, db
from project.decorators.decorators import values_comparison

with open(os.path.join(os.path.dirname(__file__), 'data_test.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def client():
    # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://travis@localhost:3306/flaskdb"
    app.config['WTF_CSRF_METHODS'] = []
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    client = app.test_client()
    db.create_all()
    # db.engine.execute(_data_sql)
    yield client


def test_empty_db(client):
    rv = client.get('/login')
    assert b'Login' in rv.data


def login(client, email, password):
    return client.post('/login', data=dict(email=email, passwd=password), follow_redirects=True)


def register_user(client, name, email, passwd, confirm, identification_number, department, charge):
    return client.post('/registration', data=dict(name=name, email=email, passwd=passwd, confirm=confirm,
                                                  identification_number=identification_number, department=department,
                                                  charge=charge))


def test_login(client):
    rv = login(client, 'pedrogrijalva@gmail.com', 'aaa')
    assert b'Hi Test!' in rv.data


def test_register(client):
    rv = register_user(client, 'Test test', 'test13@test.com', 'abc', 'abc', '0987654321', '', 'test charge')
    assert b'Test test' in rv.data


def test_validator_checkname():
    mock = MagicMock('nombre', 'nuevonombre', type='name')
    f = values_comparison(mock)
    print(type(f))

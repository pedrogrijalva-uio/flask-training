from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from project import db
from .CRUDMixin import CRUDMixin


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class User(UserMixin, CRUDMixin, Base):
    __tableName__ = 'users'
    name = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    passwd = db.Column(db.String())
    authenticated = db.Column(db.Boolean, default=False)
    identification_number = db.Column(db.String(), unique=True)
    employee = db.relationship('Employee', uselist=False, back_populates='user')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def set_password(self, password):
        self.passwd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwd_hash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.email)

    def __init__(self, name, email, passwd, identification_number):
        self.name = name
        self.email = email
        self.passwd = passwd
        self.identification_number = identification_number

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Employee(CRUDMixin, Base):
    __tableName__ = 'employees'

    charge = db.Column(db.String())
    department = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='employee')
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department', back_populates='employee')

    def __init__(self, user_id, charge, department_id):
        self.user_id = user_id
        self.charge = charge
        self.department_id = department_id

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Department(CRUDMixin, Base):
    __tableName__ = 'departments'

    name = db.Column(db.String())
    employee = db.relationship('Employee', uselist=False, back_populates='department')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

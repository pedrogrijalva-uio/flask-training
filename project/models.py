from project import db
from .db_operations import DbOperations


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class User(DbOperations, Base):
    __tableName__ = 'user'
    name = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    passwd = db.Column(db.String())
    employee = db.relationship('employee', uselist=False, back_populates='employee')
    customer = db.relationship('customer', uselist=False, back_populates='customer')

    def __init__(self, name, email, passwd):
        self.name = name
        self.email = email
        self.passwd = passwd

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Customer(Base):
    __tableName__ = 'customer'
    reception_address = db.Column(db.String())
    credit_card_number = db.Column(db.String())
    discount = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('user', back_populates='customer')

    def __init__(self, reception_address, credit_card_number, discount):
        self.reception_address = reception_address
        self.credit_card_number = credit_card_number
        self.discount = discount

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Employee(Base):
    __tableName__ = 'employee'
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    account_number = db.Column(db.String(), unique=True)
    charge = db.Column(db.String())
    department = db.relationship('department', back_populates='employee')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('user', back_populates='employee')

    def __init__(self, department, account_number, charge):
        self.department = department
        self.account_number = account_number
        self.charge = charge

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Department(Base):
    __tableName = 'department'
    name = db.Column(db.String())
    description = db.Column(db.String())
    employees = db.relationship('employee', backref=' role', lazy='dynamic')

    def __init__(self, name, description, employees):
        pass

    def __repr__(self):
        return '<id {}>'.format(self.id)

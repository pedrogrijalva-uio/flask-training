from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, validators
from wtforms.validators import DataRequired, Email

from project.enum.department_enum import DepartmentEnum


class RegistrationForm(FlaskForm):
    departments = []
    for d in DepartmentEnum:
        element = (d.value, d.name)
        departments.append(element)

    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    passwd = PasswordField('Password', validators=[DataRequired(),
                                                   validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    identification_number = StringField('SSN / CI', validators=[DataRequired()])
    department = SelectField('Department', choices=departments)
    charge = StringField('Charge', validators=[DataRequired()])
    submit = SubmitField('Register')

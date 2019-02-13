from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

from project.enum.department_enum import DepartmentEnum


class EmployeeProfileForm(FlaskForm):
    departments = []
    for d in DepartmentEnum:
        element = (d.value, d.name)
        departments.append(element)
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    identification_number = StringField('Identification Number', validators=[DataRequired()])
    department = SelectField('Department', choices=departments)
    charge = StringField('Charge', validators=[DataRequired()])
    submit = SubmitField('Update')


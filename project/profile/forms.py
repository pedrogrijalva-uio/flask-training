from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email


class EmployeeProfileForm(FlaskForm):
    departments = [('1', 'Development'),
                   ('2', 'DevOps'),
                   ('3', 'QA')]
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    identification_number = StringField('SSN / CI', validators=[DataRequired()])
    department = SelectField('Department', choices=departments)
    charge = StringField('Charge', validators=[DataRequired()])
    submit = SubmitField('Update')

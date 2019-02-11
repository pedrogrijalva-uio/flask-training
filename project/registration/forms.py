from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, validators
from wtforms.validators import DataRequired, Email


class RegistrationForm(FlaskForm):
    departments = [('1', 'Development'),
                   ('2', 'DevOps'),
                   ('3', 'QA')]
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    passwd = PasswordField('Password', validators=[DataRequired(),
                                                   validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    identification_number = StringField('SSN / CI', validators=[DataRequired()])
    department = SelectField('Department', choices=departments)
    charge = StringField('Charge', validators=[DataRequired()])
    submit = SubmitField('Register')





from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    passwd = StringField('passwd', validators=[DataRequired()])
    account = StringField('account', validators=[DataRequired()])
    charge = StringField('charge', validators=[DataRequired()])
    submit = SubmitField('Register')

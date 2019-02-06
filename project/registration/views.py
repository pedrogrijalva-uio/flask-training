from flask import render_template

from . import registration
from .forms import RegistrationForm
from ..models import Employee, User


@registration.route('/registration', methods=['GET', 'POST'])
def registrationpage():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.create(name=form.name.data,
                           email=form.email.data,
                           passwd=form.passwd.data)
        employee = Employee.create(user_id=user.id,
                        account_number=form.account.data,
                        charge=form.charge.data)

    return render_template('registration/form.html', form=form, title='Registration form')

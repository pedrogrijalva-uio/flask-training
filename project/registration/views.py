from flask import session, render_template, url_for, redirect, request
from flask_login import login_user

from . import registration
from .forms import RegistrationForm
from ..models import Employee, User


@registration.route('/registration', methods=['GET', 'POST'])
def registration_page():
    form = RegistrationForm()
    title = 'Profile registration'
    if form.validate_on_submit():
        user = User.save(name=form.name.data,
                         email=form.email.data,
                         passwd=form.passwd.data,
                         identification_number=form.identification_number.data)
        Employee.save(user_id=user.id,
                      charge=form.charge.data,
                      department_id=1)
        login_user(user)
        session['user_id'] = user.id
        return redirect(url_for(request.args.get('next', 'profile.user_data')))
    return render_template('registration/form.html', form=form, title=title)

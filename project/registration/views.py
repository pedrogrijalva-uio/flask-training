from flask import session, render_template, url_for, redirect, request, flash
from flask_login import login_user

from project.exceptions.custom_exceptions import ValueTooShort, ValueContainsSpecialCharacters
from project.validators.validators import validate_value_registration
from . import registration
from .forms import RegistrationForm
from project.services.db import user_services, employee_services


@registration.route('/registration', methods=['GET', 'POST'])
def registration_page():
    form = RegistrationForm()
    title = 'Profile registration'
    if form.validate_on_submit():
        try:
            name = validate_value_registration(form.name.data, type='name')
            identification_number = validate_value_registration(form.identification_number.data,
                                                                type='identification')
            charge = validate_value_registration(form.charge.data, type='charge')
        except ValueTooShort as exsh:
            flash(str(exsh))
        except ValueContainsSpecialCharacters as exch:
            flash(str(exch))
        else:
            user = user_services.create_user(name=name,
                                             email=form.email.data,
                                             passwd=form.passwd.data,
                                             identification_number=identification_number)

            employee_services.create_employee(user_id=user.id,
                                              charge=charge,
                                              department_id=form.department.data)
            login_user(user)
            session['user_id'] = user.id
            return redirect(url_for(request.args.get('next', 'profile.user_data')))
    return render_template('registration/form.html', form=form, title=title)

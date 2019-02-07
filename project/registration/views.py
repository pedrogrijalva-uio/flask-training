from flask import render_template
from flask_login import current_user
from . import registration
from .forms import RegistrationForm
from ..models import Employee, User, Department


@registration.route('/registration', methods=['GET', 'POST'])
def registration_page():
    form = RegistrationForm()
    update = False
    if form.validate_on_submit():
        if not update:
            user = User.create(name=form.name.data,
                               email=form.email.data,
                               passwd=form.passwd.data,
                               identification_number=form.identification_number.data)
            employee = Employee.create(user_id=user.id,
                                       charge=form.charge.data,
                                       department_id=1)
        else:
            pass
    else:
        user = User.query.filter(User.id == current_user._get_current_object().id).first()
        employee = Employee.query.filter(Employee.user_id == user.id).first()
        department = Department.query.filter(Department.id == employee.department_id).first()

        form.name.data = user.name
        form.email.data = user.email
        form.identification_number.data = user.identification_number
        form.passwd.data = user.passwd
        form.confirm.data = user.passwd
        form.charge.data = employee.charge
        form.department.data = department.id

    return render_template('registration/form.html', form=form, title='Registration form')

from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from project.exceptions.custom_exceptions import NameTooShort, NameContainsSpecialCharacters
from project.validators.validators import validate_name, validate_email, validate_identification_number
from . import profile
from .forms import EmployeeProfileForm
from ..models import User, Employee, Department


@profile.route('/user-data', methods=['GET', 'POST'])
@login_required
def user_data():
    user = User.query.get(current_user.id)
    employee = Employee.query.filter(Employee.user_id == user.id).first()
    department = Department.query.filter(Department.id == employee.department_id).first()
    return render_template('profile/employee_data.html', user=user, employee=employee, department=department)


@profile.route('/user-data/update', methods=['GET', 'POST'])
@login_required
def update_user_data():
    try:
        form = EmployeeProfileForm()
        title = 'Update profile'
        user: User = current_user
        employee: Employee = Employee.query.filter(Employee.user_id == user.id).first()
        if form.validate_on_submit():
            try:
                user.name = validate_name(form.name.data, user.name, type='name')
                user.email = validate_email(form.email.data, user.email, type='email')
                user.identification_number = validate_identification_number(form.identification_number.data,
                                                               user.identification_number, type='identification')
                employee.charge = ''
                employee.department_id = ''

                # employee.charge = values_comparison(form.charge.data, employee.charge)
                # employee.department_id = values_comparison(form.department.data, employee.department_id)
                return redirect(url_for(request.args.get('next', 'profile.user_data')))
            except NameTooShort as exsh:
                flash('User Name too short. Please type at least 5 characters')
            except NameContainsSpecialCharacters as exch:
                flash('User Name can\'t contain special characters')
            else:
                pass
                # user.update(name=user.name, email=user.email, passwd=user.passwd,
                #             identification_number=user.identification_number)
                # employee.update(user_id=user.id, charge=employee.charge, department_id=employee.department_id)
            finally:
                render_template('profile/update_employee_data.html', form=form, title=title)
        else:
            form.name.data = user.name
            form.identification_number.data = user.identification_number
            form.email.data = user.email
            form.charge.data = employee.charge
            form.department.data = Department.query.filter(Department.id == employee.department_id).first()
    except Exception as ex:
        print(ex)
    return render_template('profile/update_employee_data.html', form=form, title=title)

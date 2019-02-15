from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from project.exceptions.custom_exceptions import ValueTooShort, ValueContainsSpecialCharacters
from project.validators.validators import validate_name, validate_identification_number, \
    validate_value_changed
from . import profile
from .forms import EmployeeProfileForm
from ..models import User, Employee, Department
from ..services.rest import rest_services


@profile.route('/user-data', methods=['GET', 'POST'])
@login_required
def user_data():
    user = User.query.get(current_user.id)
    employee = Employee.query.filter(Employee.user_id == user.id).first()
    department = Department.query.filter(Department.id == employee.department_id).first()
    username = rest_services.get_github_username(user.email)
    github_username = username[0]
    github_repositories = rest_services.get_repos_by_user(username[1])
    litecoin_trx = rest_services.get_litecoin_last_transactions()
    return render_template('profile/employee_data.html', user=user, employee=employee, department=department,
                           github_username=github_username, github_repositories=github_repositories,
                           litecoin_trx=litecoin_trx)


@profile.route('/user-data/update', methods=['GET', 'POST'])
@login_required
def update_user_data():
    try:
        user: User = current_user
        form = EmployeeProfileForm()
        title = 'Update profile'
        employee: Employee = Employee.query.filter(Employee.user_id == user.id).first()
        del form.litecoin_trx
        del form.github_repositories
        del form.github_username
        if form.validate_on_submit():
            try:
                user.name = validate_name(form.name.data, user.name, type='name')
                user.email = validate_value_changed(form.email.data, user.email, type='email')
                user.identification_number = validate_identification_number(form.identification_number.data,
                                                                            user.identification_number,
                                                                            type='identification')
                employee.charge = validate_name(form.charge.data, employee.charge, type='charge')
                employee.department_id = 1
                employee.department_id = validate_value_changed(form.department.data, employee.department_id,
                                                                type='department')
            except ValueTooShort as exsh:
                flash(str(exsh))
            except ValueContainsSpecialCharacters as exch:
                flash(str(exch))
            except Exception as ex:
                flash(str(ex))
            else:
                user.update(name=user.name, email=user.email, passwd=user.passwd,
                            identification_number=user.identification_number)
                employee.update(user_id=user.id, charge=employee.charge, department_id=employee.department_id)
                return redirect(url_for(request.args.get('next', 'profile.user_data')))
            # finally:
            #     return render_template('profile/update_employee_data.html', form=form, title=title)
        else:

            form.name.data = user.name
            form.identification_number.data = user.identification_number
            form.email.data = user.email
            form.charge.data = employee.charge
            form.department.data = Department.query.filter(Department.id == employee.department_id).first()
    except Exception as ex:
        print(ex)
    return render_template('profile/update_employee_data.html', form=form, title=title)

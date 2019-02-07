from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from . import profile
from ..models import User, Employee, Department


@profile.route('/user_data', methods=['GET', 'POST'])
@login_required
def user_data():
    user = User.query.filter(User.id == current_user._get_current_object().id).first()
    employee = Employee.query.filter(Employee.user_id == user.id).first()
    department = Department.query.filter(Department.id == employee.department_id).first()
    return render_template('profile/employee_data.html', user=user, employee=employee, department=department)



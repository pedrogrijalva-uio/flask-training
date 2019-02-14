from typing import List

from project.models import Employee


def create_employee(**kw) -> Employee:
    return Employee.save(user_id=kw['id'],
                         charge=kw['charge'],
                         department_id=kw['department_id'])


def lists_employees() -> List[Employee]:
    return Employee.query.all()


def get_employee_by_user_id(user_id: int) -> Employee:
    return Employee.query.filter(Employee.user_id == user_id).first()

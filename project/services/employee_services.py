from typing import List

from ..models import Employee


def lists_employees() -> List[Employee]:
    return Employee.query.all()


def get_employee_by_user_id(user_id: int) -> Employee:
    return Employee.query.filter(Employee.user_id == user_id).first()


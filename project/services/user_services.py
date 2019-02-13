import typing

from ..models import User


def get_users() -> typing.List[User]:
    return User.query.all()


def get_user_by_email_and_password(email: str, passwd: str) -> User:
    return User.query.filter(User.email == email, User.passwd == passwd).one()

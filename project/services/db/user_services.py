import typing

from project.models import User


def create_user(**kw) -> User:
    return User.save(name=kw['name'], email=kw['email'], passwd=kw['passwd'],
                     identification_number=kw['identification_number'])


def get_users() -> typing.List[User]:
    return User.query.all()


def get_user_by_email_and_password(email: str, passwd: str) -> User:
    return User.query.filter(User.email == email, User.passwd == passwd).one()

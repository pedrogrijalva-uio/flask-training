from flask import render_template, flash, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user

from . import login
from .forms import LoginForm
from ..models import User


@login.route('/login', methods=['GET', 'POST'])
def loginuser():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter(User.email == form.email.data, User.passwd == form.passwd.data).one()
            login_user(user)
            return redirect(url_for('profile.user_data'))
        except Exception as ex:
            print(ex)
            flash('User doesn\'t exists')
    return render_template('login/form.html', form=form, title='Login')


@login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(next or url_for('/login'))

from flask import render_template, flash, url_for, redirect, request, session
from flask_login import login_user, logout_user, login_required, current_user

from project import db
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
            session['user_id'] = user.id
            return redirect(url_for(request.args.get('next', 'profile.user_data')))
        except Exception as ex:
            print(ex)
            flash('User doesn\'t exists or password is incorrect. Try again.')
    return render_template('auth/form.html', form=form, title='Login')


@login.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for(request.args.get('next', 'auth.loginuser')))

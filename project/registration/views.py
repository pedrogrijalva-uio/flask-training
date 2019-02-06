from flask import render_template

from . import registration


@registration.route('/')
def rergistrationpage():
    return render_template('registration/form.html', title='Registration form')

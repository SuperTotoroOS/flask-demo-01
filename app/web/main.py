"""
Created by Ricky Yang on 7/10/19
@File: main.py
@Description:
"""
from flask import render_template
from flask_login import login_required, current_user

from . import web


@web.route('/')
@login_required
def index():
    user = current_user
    return render_template('pages/index.html', user=user)


@web.route('/user')
@login_required
def user_details():
    user = current_user
    return render_template('pages/user-details.html', user=user)

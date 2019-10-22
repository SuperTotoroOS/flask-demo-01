"""
Created by Ricky Yang on 7/10/19
@File: user.py
@Description: 用户操作
"""
from flask import render_template, jsonify
from flask_login import login_required, current_user

from . import web


@web.route('/user')
@login_required
def get_user():
    user = current_user
    return render_template('pages/user-details.html', user=user)

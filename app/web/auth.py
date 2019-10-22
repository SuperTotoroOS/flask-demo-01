"""
Created by Ricky Yang on 8/10/19
@File: auth.py
@Description: 注册登录
"""

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, current_user, logout_user
from app.libs.email import send_mail

from app.models.base import db
from app.models.user import User
from app.validators.auth import RegisterForm, LoginForm, EmailForm, ChangePasswordForm, ResetPasswordForm
from . import web


@web.route('/')
@login_required
def index():
    user = current_user
    return render_template('pages/index.html', user=user)


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('pages/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            current = request.args.get('next')
            if not current or not current.startswith('/'):
                current = url_for('web.index')
            return redirect(current)
        else:
            flash('Email or password incorrect')
    return render_template('pages/login.html', form=form)


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.login'))


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email=account_email).first_or_404()
            send_mail(form.email.data, 'Reset your password', 'email/reset_password.html',
                      user=user, token=user.generate_token())
            flash('Please check in your Email: ' + account_email)
    return render_template('pages/forget-password-request.html', form=form)


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        success = User.reset_password(token, form.password1.data)
        if success:
            flash('Your password has been reset')
            return redirect(url_for('web.login'))
        else:
            flash('We can not reset your password')
    return render_template('pages/forget-password.html')


@web.route('/change/password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        user = current_user
        if user and user.check_password(form.old_password.data):
            with db.auto_commit():
                user.password = form.new_password1.data
                flash('Password has been updated')
                return redirect(url_for('web.user_details'))
        else:
            flash('Please input correct password')
    return render_template('pages/change_password.html', form=form)








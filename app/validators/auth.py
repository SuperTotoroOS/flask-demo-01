from wtforms import Form, StringField, PasswordField
from wtforms.validators import EqualTo, Length, DataRequired, Email, ValidationError

from app.models.user import User
from app.validators.base import BaseForm


class RegisterForm(BaseForm):
    email = StringField(validators=[
        DataRequired(), Length(8, 64), Email(message='Invalid email')])

    password = PasswordField(validators=[
        DataRequired(message='Password are not allowed to empty'), Length(6, 32)])

    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='Invalid email length')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email has been registered')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('Nickname has existed')


class LoginForm(Form):
    email = StringField(validators=[
        DataRequired(), Length(8, 64), Email(message='Invalid email')])
    password = PasswordField(validators=[
        DataRequired(message='Password are not allowed to empty'), Length(6, 32)])


class EmailForm(Form):
    email = StringField(validators=[
        DataRequired(), Length(8, 64), Email(message='Invalid email')])


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(), Length(6, 32, message='Invalid password length'),
        EqualTo('password2', message='Passwords are different')])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)])


class ChangePasswordForm(Form):
    old_password = PasswordField(validators=[DataRequired()])
    new_password1 = PasswordField(validators=[
        DataRequired(), Length(6, 32, message='Invalid password length'),
        EqualTo('new_password2', message='Passwords are different')])
    new_password2 = PasswordField(validators=[DataRequired()])

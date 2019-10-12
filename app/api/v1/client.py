"""
Created by Ricky Yang on 11/10/19
@File: client.py
@Description:
"""
from flask import request

from app.lib.enums import ClientTypeEnum
from app.lib.redprint import Redprint
from app.models.user import User
from app.validators.client import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email
        }
        promise[form.type.data]()
    return 'success'


def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data, form.account.data, form.secret.data)


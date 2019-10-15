"""
Created by Ricky Yang on 11/10/19
@File: client.py
@Description: 客户端注册
"""
from app.lib.enums import ClientTypeEnum
from app.lib.error_code import CreateSuccess
from app.lib.redprint import Redprint
from app.models.user import User
from app.validators.client import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return CreateSuccess()


@api.route('', methods=['PUT'])
def update_client():
    pass


@api.route('', methods=['GET'])
def get_client():
    pass


@api.route('', methods=['DELETE'])
def delete_client():
    pass


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)


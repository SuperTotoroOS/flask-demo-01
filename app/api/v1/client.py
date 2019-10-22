"""
Created by Ricky Yang on 11/10/19
@File: client.py
@Description: 客户端注册API
    create_client(/v1/client, POST, account&secret&type): 创建客户端
"""
from app.libs.enums import ClientTypeEnum
from app.libs.error_code_api import CreateSuccess
from app.libs.module import Module
from app.models.user import User
from app.validators.client import ClientForm, UserEmailForm

api = Module('client')


@api.route('', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return CreateSuccess()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)


def __register_user_by_mobile():
    pass


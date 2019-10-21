"""
Created by Ricky Yang on 13/10/19
@File: token.py
@Description: Token操作API
    get_token(/v1/token, POST, account&secret&type): 获取token
    get_token_info(/v1/info, POST, token): 获取token信息
"""
from flask import current_app, jsonify

from app.lib.error_code_api import AuthFailed
from app.lib.module import Module
from app.models.user import User
from app.validators.client import ClientForm, TokenForm
from app.lib.enums import ClientTypeEnum
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

api = Module('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'], form.type.data, identity['scope'], expiration)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


@api.route('/info', methods=['POST'])
def get_token_info():
    form = TokenForm().validate_for_api()
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(form.token.data, return_header=True)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)

    r = {
        'scope': data[0]['scope'],
        'create_at': data[1]['iat'],
        'expire_in': data[1]['exp'],
        'uid': data[0]['uid']
    }
    return jsonify(r)


# 生成token方法
def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })


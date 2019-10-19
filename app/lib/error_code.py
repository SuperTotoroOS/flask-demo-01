"""
Created by Ricky Yang on 12/10/19
@File: error_code.py
@Description: 状态码
"""
from app.lib.errors import APIException


class Success(APIException):
    code = 200
    msg = 'success'
    error_code = 0


class CreateSuccess(Success):
    code = 201


class DeleteSuccess(Success):
    code = 202
    error_code = -1


class ServerException(APIException):
    code = 500
    msg = 'server error'
    error_code = 999


class ClientTypeException(APIException):
    code = 400
    msg = 'client type is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'parameter is invalid'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'resource is not be found'
    error_code = 1001


# 授权失败，账号密码出错
class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005


# 权限不够
class Forbidden(APIException):
    code = 403
    msg = 'authorization failed'
    error_code = 1005
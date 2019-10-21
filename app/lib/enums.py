"""
Created by Ricky Yang on 11/10/19
@File: enums.py
@Description: 客户端注册类型
    USER_EMAIL: 邮箱注册
    USER_MOBILE: 手机号注册
    USER_FACEBOOK: facebook授权
    USER_TWITTER: twitter授权
"""
from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    USER_FACEBOOK = 200
    USER_TWITTER = 201


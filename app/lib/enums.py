"""
Created by Ricky Yang on 11/10/19
@File: enums.py
@Description:
"""
from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    USER_FACEBOOK = 200
    USER_TWITTER = 201


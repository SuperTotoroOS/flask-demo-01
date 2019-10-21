"""
Created by Ricky Yang on 11/10/19
@File: __init__.py
@Description: 将Module中的API注册到蓝图上
"""
from flask import Blueprint
from app.api.v1 import user, client, token


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    user.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    return bp_v1

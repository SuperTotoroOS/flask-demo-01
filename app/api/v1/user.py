"""
Created by Ricky Yang on 11/10/19
@File: user.py
@Description: 用户操作API
    create_user: 创建用户
    update_user: 修改用户信息（需要登录）
    get_user(/v1/user, GET): 获取用户（需要登录）
    delete_user(/v1/user, DELETE): 删除用户（需要登录）
    super_get_user(/v1/user, GET, uid): 超级管理员获取用户
    super_delete_user(/v1/user, DELETE, uid): 超级管理员删除用户
"""
from flask import jsonify, g

from app.libs.error_code_api import DeleteSuccess
from app.models.base import db
from app.libs.module import Module
from app.libs.token_auth import auth
from app.models.user import User

api = Module('user')


@api.route('', methods=['POST'])
def create_user():
    pass


@auth.login_required
@api.route('', methods=['PUT'])
def update_user():
    pass


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404(uid)
    return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404(uid)
        user.delete()
    return DeleteSuccess()


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404(uid)
    return jsonify(user)


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user():
    pass




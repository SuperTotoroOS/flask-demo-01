"""
Created by Ricky Yang on 11/10/19
@File: user.py
@Description:
"""
from flask import jsonify

from app.lib.error_code import DeleteSuccess
from app.models.base import db
from app.lib.redprint import Redprint
from app.lib.token_auth import auth
from app.models.user import User

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user)


@api.route('/<int:uid>', methods=['POST'])
@auth.login_required
def create_user():
    pass


@api.route('', methods=['PUT'])
def update_user():
    pass


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def delete_user(uid):
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404(uid)
        user.delete()
    return DeleteSuccess()




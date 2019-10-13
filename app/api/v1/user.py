"""
Created by Ricky Yang on 11/10/19
@File: user.py
@Description:
"""
from app.lib.redprint import Redprint
from app.lib.token_auth import auth
from app.models.user import User

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    return user


@api.route('', methods=['POST'])
def create_user():
    pass


@api.route('', methods=['PUT'])
def update_user():
    pass


@api.route('', methods=['DELETE'])
def delete_user():
    pass




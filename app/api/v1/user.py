"""
Created by Ricky Yang on 11/10/19
@File: user.py
@Description:
"""
from app.lib.redprint import Redprint

api = Redprint('user')


@api.route('', methods=['POST'])
def create_user():
    pass


@api.route('', methods=['PUT'])
def update_user():
    pass


@api.route('', methods=['DELETE'])
def delete_user():
    pass


@api.route('', methods=['GET'])
def get_user():
    pass

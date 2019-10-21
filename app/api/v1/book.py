"""
Created by Ricky Yang on 11/10/19
@File: book.py
@Description:
"""
from app.lib.redprint import Redprint

api = Redprint('book')


@api.route('', methods=['GET'])
def get_book():
    pass


@api.route('', methods=['POST'])
def create_book():
    pass

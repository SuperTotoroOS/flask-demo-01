"""
Created by Ricky Yang on 15/10/19
@File: app.py.py
@Description:
"""
from datetime import date
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from app.libs.error_code_api import ServerException


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerException()


class Flask(_Flask):
    json_encoder = JSONEncoder

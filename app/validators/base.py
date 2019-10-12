"""
Created by Ricky Yang on 12/10/19
@File: base.py
@Description:
"""
from flask import request
from wtforms import Form

from app.lib.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        super(BaseForm, self).__init__(data=request.json)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self

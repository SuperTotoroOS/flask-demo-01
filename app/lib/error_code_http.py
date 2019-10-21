"""
Created by Ricky Yang on 20/10/19
@File: error_code_http.py
@Description:
"""
from werkzeug.exceptions import HTTPException


class NotFound(HTTPException):
    code = 404
    msg = 'resource is not be found'
    error_code = 1001
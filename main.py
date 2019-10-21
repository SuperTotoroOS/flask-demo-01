"""
Created by Ricky Yang on 5/10/19
@File: main.py
@Description: 项目启动文件
"""
from http.client import HTTPException

from flask import render_template

from app import create_app
from app.lib.error_code_api import ServerException
from app.lib.customize_api_exception import APIException


app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    a = 1
    if isinstance(e, HTTPException):
        error = {
            'code': e.code,
            'msg': e.description,
            'error_code': 1007,
        }
        return render_template('pages/404.html', error=error)
    if isinstance(e, APIException):
        return e
    else:
        if not app.config['DEBUG']:
            return ServerException()
        else:
            raise e


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'], threaded=True)

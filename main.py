"""
Created by Ricky Yang on 5/10/19
@File: main.py
@Description: 项目启动文件
"""
from http.client import HTTPException

from app import create_app
from app.lib.error_code import ServerException
from app.lib.errors import APIException


app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        if not app.config['DEBUG']:
            return ServerException()
        else:
            raise e


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'], threaded=True)

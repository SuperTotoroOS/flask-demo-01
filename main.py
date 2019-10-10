"""
Created by Ricky Yang on 5/10/19
@File: main.py
@Description: 项目启动文件
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'], threaded=True)

"""
Created by Ricky Yang on 5/10/19
@File: __init__.py
@Description: 项目入口文件
"""
from flask import Flask
from flask_login import LoginManager
# from app._libs.limiter import Limiter
from app.models.base import db

login_manager = LoginManager()
# mail = Mail()
# # cache = Cache(config={'CACHE_TYPE': 'simple'})
# limiter = Limiter()


def create_app():
    # 实例化Flask对象
    app = Flask(__name__)  # template_folder='web/fisher/_templates'

    # 载入配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    # 注册蓝图
    register_blueprint(app)

    # 加载flask_login
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = 'Please Login First'

    # mail.init_app(app)

    # 初始化数据库
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

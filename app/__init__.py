"""
Created by Ricky Yang on 5/10/19
@File: __init__.py
@Description: 项目入口文件
"""
from flask_login import LoginManager
from flask_mail import Mail

from .app import Flask

login_manager = LoginManager()
mail = Mail()


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_database(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def register_flask_login(app):
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = 'Please Login First'


# def register_flask_mail(app):
#     mail.init_app(app)


def create_app():
    # 实例化Flask对象
    app = Flask(__name__)

    # 载入配置文件
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    # 注册蓝图
    register_blueprint(app)

    # 加载数据库
    register_database(app)

    # 加载flask_login
    register_flask_login(app)

    # 加载flask_mail
    mail.init_app(app)

    return app










"""
Created by Ricky Yang on 8/10/19
@File: user.py
@Description: 用户类
"""

from flask import current_app
from flask_login import UserMixin
from sqlalchemy import Column, String, Boolean, SmallInteger, Integer
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import login_manager
from app.lib.error_code import NotFound, AuthFailed
from app.models.base import Base, db


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(32), nullable=False)
    avatar = Column(String(128))
    _password = Column('password', String(128), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(64), unique=True, nullable=False)
    address = Column(String(256))
    confirmed = Column(Boolean, default=False)
    auth = Column(SmallInteger, default=1)  # 用户权限；0 超级管理员 2 管理员 1 普通用户

    facebook = Column(String(64))
    twitter = Column(String(64))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False

        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        return {'uid': user.id}

    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({
            'uid': uid,
            'type': ac_type.value
        }).decode('utf-8')

    def summary(self):
        return dict(
            nickname=self.nickname,
            username=self.username,
        )


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))

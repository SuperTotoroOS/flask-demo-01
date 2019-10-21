"""
Created by Ricky Yang on 16/10/19
@File: fake.py
@Description:
"""
import time

from app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()

count = 0


def create_user(count):
    for i in range(10):
        count += 1
        username = 'user_' + str(count)
        account = username + '@ad.unsw.edu.au'
        generate_fake_user(username, account)


def generate_fake_user(username, account):
    with app.app_context():
        with db.auto_commit():
            user = User()
            user.nickname = username
            user.email = account
            user.password = '123456'
            user.auth = 1
            db.session.add(user)


create_user(count)





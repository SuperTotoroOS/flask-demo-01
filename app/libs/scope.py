"""
Created by Ricky Yang on 16/10/19
@File: scope.py
@Description: 用户权限，根据权限返回可以访问的接口
"""


class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    # 运算符重载，支持两个对象相加
    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))
        return self


class UserScope(Scope):
    # allow_api = ['v1.user+get_user', 'v1.user+delete_user']
    allow_module = ['v1.user']
    forbidden = ['v1.user+super_get_user', 'v1.user+super_delete_user']


class AdminScope(Scope):
    # allow_api = ['v1.user+super_get_user', 'v1.user+super_delete_user']
    allow_module = ['v1.user']

    def __init__(self):
        self + UserScope()


class SuperScope(Scope):
    # allow_api = []
    allow_module = ['v1.user']

    def __init__(self):
        self + UserScope() + AdminScope()


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    split = endpoint.split('+')
    module_name = split[0]
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if module_name in scope.allow_module:
        return True
    else:
        return False

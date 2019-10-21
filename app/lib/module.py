"""
Created by Ricky Yang on 11/10/19
@File: module.py
@Description: 自定义蓝图
"""


class Module:
    def __init__(self, name):
        self.name = name
        self.mound = []

    # 把视图函数注册到蓝图上
    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f
        return decorator

    # 注册蓝图
    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name

        for f, rule, options in self.mound:
            endpoint = self.name + '+' + options.pop('endpoint', f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
            pass
        pass

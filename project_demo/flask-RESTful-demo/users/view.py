# -*- encoding: utf-8 -*-
"""
@File : view
@Time : 2020/6/22 21:11
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from app import app
# here put the import lib


@app.route('/')
def home():
    return 'user.home'
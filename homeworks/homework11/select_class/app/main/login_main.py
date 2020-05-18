# -*- encoding: utf-8 -*-
"""
@File : login_main
@Time : 2020/5/18 22:46
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from flask_login import UserMixin
from app import login_manager
from models import User
# here put the import lib


@login.user_loader
def load_user(name):
    return User.query.get(name)
# -*- encoding: utf-8 -*-
"""
@File : __init__.py
@Time : 2020/6/22 21:10
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
# here put the import lib
from flask import Blueprint

users=Blueprint('users',__name__)
user_blu = Blueprint("users",__name__,static_folder='static_users')
from .view import *
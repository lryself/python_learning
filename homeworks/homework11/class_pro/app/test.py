# -*- encoding: utf-8 -*-
"""
@File : other
@Time : 2020/6/15 16:56
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
# here put the import lib
from werkzeug.security import generate_password_hash
from flask import url_for


if __name__ == '__main__':
    print(url_for('/login', next_url='url'))
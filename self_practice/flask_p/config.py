# -*- encoding: utf-8 -*-
"""
@File : config
@Time : 2020/5/17 19:17
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
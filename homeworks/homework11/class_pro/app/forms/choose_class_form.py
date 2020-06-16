# -*- encoding: utf-8 -*-
"""
@File : choose_class_form
@Time : 2020/6/15 23:48
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField
# here put the import lib


class ClassFrom(FlaskForm):
    submit = SubmitField('选择')
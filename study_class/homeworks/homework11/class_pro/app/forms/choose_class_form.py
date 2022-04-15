# -*- encoding: utf-8 -*-
"""
@File : choose_class_form
@Time : 2020/6/15 23:48
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators
# here put the import lib


class ClassFrom(FlaskForm):
    class_id=StringField('请输入课程代号：', validators=[validators.DataRequired(message="课程代号不能为空")])
    submit = SubmitField('选择')
    del_class = SubmitField('退课')
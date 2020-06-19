# -*- encoding: utf-8 -*-
"""
@File : auth_class
@Time : 2020/6/17 22:58
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators, BooleanField
# here put the import lib


class UserFrom(FlaskForm):
    name=StringField('请输入用户姓名：')
    password=StringField('请输入用户密码：')
    is_student=BooleanField('学生身份', default=True)
    submit = SubmitField('添加用户')
    del_user = SubmitField('删除用户')
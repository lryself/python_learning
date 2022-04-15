# -*- encoding: utf-8 -*-
"""
@File : sign_in
@Time : 2020/6/14 22:15
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo
# here put the import lib


class LoginForm(FlaskForm):
    username = StringField('用户名：', validators=[DataRequired(message="用户名不能为空")])
    password = PasswordField('密码：', validators=[DataRequired(message="密码不能为空")])
    submit = SubmitField('登录')


# class RegistrationForm(FlaskForm):
#     username = StringField('用户名', validators=[DataRequired()])
#     password = PasswordField('密码', validators=[DataRequired()])
#     password2 = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('注册')
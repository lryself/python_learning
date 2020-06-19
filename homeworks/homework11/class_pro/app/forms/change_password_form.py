# -*- encoding: utf-8 -*-
"""
@File : change_password_form
@Time : 2020/6/20 0:23
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
# here put the import lib
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo
# here put the import lib


class ChangeForm(FlaskForm):
    password = PasswordField('旧密码：', validators=[DataRequired(message="密码不能为空")])
    new_password = PasswordField('新密码', validators=[DataRequired()])
    new_password2 = PasswordField('重复新密码', validators=[DataRequired(), EqualTo('new_password', message="两次密码不一致")])
    submit = SubmitField('修改')
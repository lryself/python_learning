# -*- encoding: utf-8 -*-
"""
@File : auth_class
@Time : 2020/6/17 22:58
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators
# here put the import lib


class ClassFrom(FlaskForm):
    class_id=StringField('请输入课程编号：')
    class_name=StringField('请输入课程名称：')
    class_teacher=StringField('请输入课程教师：')
    class_time=StringField('请输入课程时间：')
    class_begin_week=StringField('请输入课程开始周数：')
    class_end_week=StringField('请输入课程结束周数：')
    submit = SubmitField('添加课程')
    del_class = SubmitField('删除课程')
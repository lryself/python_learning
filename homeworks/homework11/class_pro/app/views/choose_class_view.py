# -*- encoding: utf-8 -*-
"""
@File : choose_class
@Time : 2020/6/15 23:29
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from app import app, require_login
from wtforms import SubmitField
from models.ClassesModel import Classes
from flask import render_template
# here put the import lib


@app.route('/choose_class',methods=('GET', 'POST'))
@require_login('/choose_class')
def choose_class():
    classes=[]
    temp=Classes.find_class('all')
    submit = SubmitField('选择')
    return render_template('choose_class.html')

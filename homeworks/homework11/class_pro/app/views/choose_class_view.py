# -*- encoding: utf-8 -*-
"""
@File : choose_class
@Time : 2020/6/15 23:29
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from app import app
from wtforms import SubmitField
from models.ClassesModel import Classes
from flask import render_template
from forms.choose_class_form import ClassFrom
from flask_login import login_required
# here put the import lib


@app.route('/choose_class', methods=('GET', 'POST'))
@login_required
def choose_class():
    form=ClassFrom()
    classes=[]
    temp=Classes.find_class('all')
    weekday=["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    for i in temp:
        times=i.time.split("|")
        time_str=''
        for j in times:
            time_str+='{} 第{}节\n'.format(weekday[int(j[0])],j[2])
        temp_dir={'id': i.id,
                  'name': i.name,
                  'teacher': i.teacher,
                  'time': '第{}周-第{}周 {}'.format(i.begin_week,i.end_week,time_str)}
        classes.append(temp_dir)
    return render_template('choose_class.html', classes=classes, form=form)

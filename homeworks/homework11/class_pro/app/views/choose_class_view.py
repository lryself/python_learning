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
from flask import render_template, flash, redirect, url_for
from forms.choose_class_form import ClassFrom
from flask_login import login_required, current_user
# here put the import lib


@app.route('/choose_class', methods=('GET', 'POST'), endpoint='choose_class')
@login_required
def choose_class():
    form = ClassFrom()
    if form.validate_on_submit():
        if form.submit.data:
            class_id = form.class_id.data
            res = current_user.add_class(class_id)
            if res:
                flash('{}课程选择成功！'.format(class_id))
            else:
                flash('{}课程选择失败！'.format(class_id))
        if form.del_class.data:
            class_id = form.class_id.data
            res = current_user.del_class(class_id)
            if res:
                flash('{}课程退选成功！'.format(class_id))
            else:
                flash('{}课程退选失败！'.format(class_id))
        return redirect(url_for('choose_class'))
    classes=[]
    temp=Classes.find_class('all')
    weekday=["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    for i in temp:
        times=i.time.split("|")
        time_str=''
        for j in times:
            time_str+='{} 第{}节\n'.format(weekday[int(j[0])], j[2])
        if i.id in current_user.classes:
            temp_str='已选'
        else:
            temp_str='未选'
        temp_dir={'id': i.id,
                  'name': i.name,
                  'teacher': i.teacher,
                  'time': '第{}周-第{}周 {}'.format(i.begin_week, i.end_week, time_str),
                  'choose': temp_str
                  }
        classes.append(temp_dir)
    return render_template('choose_class.html', classes=classes, form=form)

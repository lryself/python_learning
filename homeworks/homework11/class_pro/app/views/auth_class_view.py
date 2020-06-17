# -*- encoding: utf-8 -*-
"""
@File : auth_class_view
@Time : 2020/6/17 22:57
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from app import app
from models.ClassesModel import Classes
from flask import render_template, flash, redirect, url_for
from forms.auth_class_form import ClassFrom
from flask_login import login_required, current_user

# here put the import lib


@app.route('/auth_class', methods=('GET', 'POST'), endpoint='auth_class')
@login_required
def choose_class():
    form = ClassFrom()
    if form.validate_on_submit():
        class_id=form.class_id.data
        class_name=form.class_name.data
        class_teacher=form.class_teacher.data
        class_time=form.class_time.data
        class_begin_week=form.class_begin_week.data
        class_end_week=form.class_end_week.data
        if form.submit.data:
            res = current_user.additive_class(class_teacher=class_teacher,
                                              class_name=class_name,
                                              class_time=class_time,
                                              class_begin_week=class_begin_week,
                                              class_end_week=class_end_week
                                              )
            if res:
                flash('{}课程添加成功！'.format(class_name))
            else:
                flash('{}课程添加失败！'.format(class_name))
        if form.del_class.data:
            res = current_user.delete_class(class_id)
            if res:
                flash('{}课程删除成功！'.format(class_id))
            else:
                flash('{}课程删除失败！'.format(class_id))
        return redirect(url_for('auth_class'))
    classes = []
    temp = Classes.find_class('all')
    weekday = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    for i in temp:
        times = i.time.split("|")
        time_str = ''
        for j in times:
            time_str += '{} 第{}节\n'.format(weekday[int(j[0])-1], j[2])
        temp_dir = {'id': i.id,
                    'name': i.name,
                    'teacher': i.teacher,
                    'time': '第{}周-第{}周 {}'.format(i.begin_week, i.end_week, time_str),
                    'choose': '正常'
                    }
        classes.append(temp_dir)
    return render_template('auth_class.html', classes=classes, form=form)
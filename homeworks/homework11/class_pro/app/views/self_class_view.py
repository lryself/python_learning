# -*- encoding: utf-8 -*-
"""
@File : self_class_view
@Time : 2020/6/17 21:48
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
# here put the import lib
from app import app
from flask_login import login_required, current_user
from forms.self_class_form import SelfclassModel
from models import ClassesModel
from flask import render_template


@app.route('/self_class', methods=('GET', 'POST'), endpoint='self_class')
@login_required
def self_class():
    form = SelfclassModel()
    if form.validate_on_submit():
        pass
    classes = []
    weekday = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    week_class = [[[''] for col in range(8)] for row in range(10)]
    for i in current_user.classes:
        cls = ClassesModel.Classes.find_class(word='id', value=i)[0]
        cls_times = cls.time.split('|')
        time_str = ''
        for j in cls_times:
            time_str += '{} 第{}节\n'.format(weekday[int(j[0])], j[2])
        temp_dir = {'id': cls.id, 'name': cls.name, 'teacher': cls.teacher,
                    'time': '第{}周-第{}周 {}'.format(cls.begin_week, cls.end_week, time_str)}
        classes.append(temp_dir)

        for w in cls_times:
            week, num = w.split('_')
            week_class[int(num) - 1][int(week)].append(cls.name)

    for i in range(10):
        week_class[i][0].append(str(i + 1))
    classes = sorted(classes, key=lambda x: x['id'])
    return render_template('self_class.html', week_classes=week_class, form=form, username=current_user.username,
                           classes=classes)

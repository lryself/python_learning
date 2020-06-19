# -*- encoding: utf-8 -*-
"""
@File : auth_class_view
@Time : 2020/6/17 22:57
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from app import app
from models.UserModel import User
from flask import render_template, flash, redirect, url_for
from forms.auth_user_form import UserFrom
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash

# here put the import lib


@app.route('/auth_user', methods=('GET', 'POST'), endpoint='auth_user')
@login_required
def auth_user():
    form = UserFrom()
    if form.validate_on_submit():
        username = form.name.data
        password = generate_password_hash(form.password.data)
        if form.is_student.data:
            is_student = 1
        else:
            is_student = 0
        if form.submit.data:
            res = current_user.additive_user(username=username,
                                             password=password,
                                             is_student=is_student)
            if res:
                flash('{}用户添加成功！'.format(username))
            else:
                flash('{}用户添加失败！'.format(username))
        if form.del_user.data:
            res = current_user.delete_user(username)
            if res:
                flash('{}用户删除成功！'.format(username))
            else:
                flash('{}用户删除失败！'.format(username))
        return redirect(url_for('auth_user'))
    users = User.find_stu('all')
    users = sorted(users, key=lambda x: x.is_student)
    return render_template('auth_user.html', users=users, form=form)

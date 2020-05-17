# -*- encoding: utf-8 -*-
"""
@File : main
@Time : 2020/5/17 18:35
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
"""
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, oid
from app.forms.login_registration import LoginForm
from app.main.User import Userself

@app.route('/login', methods=('GET', 'POST'))  # 登录
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        is_student=form.is_student.data
        ems=None
        if Userself.load(username=user_name, password=password): # 从用户数据中查找用户记录
            user = Userself(user_name, password, is_student)  # 创建用户实体
            login_user(user)  # 创建用户 Session
            return redirect(request.args.get('next') or url_for('index'))
        else:
            ems = "用户名或密码密码有误"
    return render_template('login.html', form=form, emsg=ems)


# @app.route('/login', methods=['GET', 'POST'])
# @oid.loginhandler
# def login():
#     if g.user is not None and g.user.is_authenticated():
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         session['is_student'] = form.is_student.data
#         return oid.try_login(form.openid.data, ask_for=['name'])
#     return render_template('login.html',title='登录页面',form=form,providers=app.config['OPENID_PROVIDERS'])


# @oid.after_login
# def after_login(resp):
#     if resp.name is None or resp.name == "":
#         flash('用户名为空，请重新输入')
#         return redirect(url_for('login'))
#     user = User.query.filter_by(name=resp.name).first()
#     if user is None:
#         nickname = resp.nickname
#         if nickname is None or nickname == "":
#             nickname = resp.email.split('@')[0]
#         user = User(nickname=nickname, email=resp.email)
#         db.session.add(user)
#         db.session.commit()
#     remember_me = False
#     if 'remember_me' in session:
#         remember_me = session['remember_me']
#         session.pop('remember_me', None)
#     login_user(user, remember = remember_me)
#     return redirect(request.args.get('next') or url_for('index'))


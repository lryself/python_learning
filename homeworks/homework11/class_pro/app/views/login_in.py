# -*- encoding: utf-8 -*-
from forms.login import LoginForm
from flask import render_template
from app import app, login_user
from models.UserselfModel import Userself


@app.route('/', methods=('GET', 'POST'))
@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    ems=''
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        if Userself.load(username=user_name, password=password): # 从用户数据中查找用户记录
            login_user(user_name, password)  # 创建用户
            return render_template('index.html')
        else:
            ems = "用户名或密码密码有误"
    return render_template('login_in.html', form=form, emsg=ems)
# -*- encoding: utf-8 -*-
from forms.login import LoginForm
from flask import render_template, flash, redirect, url_for, g, request
from models.UserselfModel import Userself
from app import app, login_manager
from models.UserModel import User
from flask_login import login_user

@app.route('/login', methods=('GET', 'POST'), endpoint='login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        if Userself.load(username=user_name, password=password): # 从用户数据中查找用户记录
            g.user = Userself(user_name, password)
            user=User.find_stu(value=user_name)
            login_user(user)
            next_url = request.args.get('next')
            return redirect(next_url or url_for('index'))
        else:
            flash('用户名或密码密码有误')
    return render_template('login_in.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    user=User.find_stu(value=user_id)
    return user
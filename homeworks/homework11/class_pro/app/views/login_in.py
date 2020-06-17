# -*- encoding: utf-8 -*-
from werkzeug.urls import url_parse

from forms.login_form import LoginForm
from flask import render_template, flash, redirect, url_for, g, request
from models.UserselfModel import Userself
from app import app
from flask_login import login_user


@app.route('/login', methods=('GET', 'POST'), endpoint='login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        if Userself.load(username=user_name, password=password):  # 从用户数据中查找用户记录
            user = Userself(user_name)
            login_user(user)
            next_url = request.args.get('next')
            if not next_url or url_parse(next_url).netloc != '':
                next_url = url_for('index')
            return redirect(next_url)
        else:
            flash('用户名或密码密码有误')
    return render_template('login_in.html', form=form)



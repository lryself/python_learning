# -*- encoding: utf-8 -*-
from werkzeug.urls import url_parse

from forms.change_password_form import ChangeForm
from flask import render_template, flash, redirect, url_for, g, request
from models.UserselfModel import Userself
from app import app
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/change_password', methods=('GET', 'POST'), endpoint='change_password')
@login_required
def change_password():
    form = ChangeForm()
    if form.validate_on_submit():
        password = form.password.data
        new_password = form.new_password.data
        if current_user.upd_password(password, new_password):
            logout_user()
            return redirect('/')
        else:
            flash('旧密码有误')
    return render_template('change_password.html', form=form)



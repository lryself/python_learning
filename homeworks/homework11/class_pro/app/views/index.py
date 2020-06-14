# -*- encoding: utf-8 -*-

from flask import render_template
from app import user, app
# here put the import lib


@app.route('/index')
def index():
    text = "首页"
    return render_template('index.html', title=user.username, text=text)
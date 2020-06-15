# -*- encoding: utf-8 -*-

from flask import render_template
from app import app, require_login
# here put the import lib


@app.route('/', endpoint='index')
@app.route('/index', endpoint='index')
@require_login('index')
def index():
    text = "首页"
    from app import user
    return render_template('index.html', title=user.username, text=text)
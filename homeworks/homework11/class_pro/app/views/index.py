# -*- encoding: utf-8 -*-

from flask import render_template
from app import app
from flask_login import login_required
# here put the import lib


@app.route('/', endpoint='index')
@app.route('/index', endpoint='index')
@login_required
def index():
    return render_template('index.html')
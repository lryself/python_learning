# -*- encoding: utf-8 -*-
"""
@File : main
@Time : 2020/5/20 8:34
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from app import app
from flask import g
# here put the import lib


@app.before_request
def before_request():
    g.db = sqlite3.connect(app.config['DATABASE'])



@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
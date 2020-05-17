# -*- encoding: utf-8 -*-
"""
@File : __init__.py
@Time : 2020/5/16 11:18
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from flask import Flask
import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# here put the import lib
app = Flask(__name__)


login = LoginManager()
login.init_app(app)
login.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.forms import *
from app.views import main, login
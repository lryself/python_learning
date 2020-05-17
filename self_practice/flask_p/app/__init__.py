# -*- encoding: utf-8 -*-
"""
@File : __init__.py
@Time : 2020/5/17 18:54
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models

# -*- encoding: utf-8 -*-
from flask import Flask, g
import config
from flask_migrate import Migrate
# here put the import lib

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = '请登录！'
login_manager.init_app(app)

from flask import redirect, url_for
from app import models

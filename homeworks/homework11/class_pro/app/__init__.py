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


from models.UserselfModel import Userself
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = '请登录！'
login_manager.init_app(app)

from flask import redirect, url_for


# def require_login(url):
#     def get_func(func):
#         def wrap(*args):
#             if not g.user_logined:
#                 return redirect(url_for('login', next_url=url))
#             return func(*args)
#         return wrap
#     return get_func

from app.views import login_in, index, choose_class_view
from app import models

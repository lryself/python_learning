# -*- encoding: utf-8 -*-
from flask import Flask
import config
from flask_migrate import Migrate
# here put the import lib

app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models.UserselfModel import Userself
user = None
user_logined=False


def login_user(user_name, password):
    global user, user_logined
    user = Userself(user_name, password)
    user_logined=True


from flask import redirect, url_for


def require_login(url):
    def get_func(func):
        def wrap(*args):
            global user_logined
            if not user_logined:
                return redirect(url_for('login', next_url=url))
            return func(*args)
        return wrap
    return get_func

from app.views import login_in, index
from app import models

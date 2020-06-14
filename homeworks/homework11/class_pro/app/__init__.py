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


def login_user(user_name, password):
    global user
    user = Userself(user_name, password)


from app.views import login_in, index
from app import models

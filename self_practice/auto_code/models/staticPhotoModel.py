# coding: utf-8
from . import db


class StaticPhoto(db.Model):
    __tablename__ = 'static_photo'
    Auto = db.Column(db.Integer, primary_key=True, info='自动编号')
    photoID = db.Column(db.String(20), nullable=False, info='图片编号')
    photoUrl = db.Column(db.String(255), nullable=False, info='云储存图片网址')

# coding: utf-8
from . import db


class MessageInfo(db.Model):
    __tablename__ = 'message_info'
    AutoID = db.Column(db.Integer, primary_key=True, info='自动编号')
    messageID = db.Column(db.String(20), info='消息编号')
    messageTitle = db.Column(db.String(255), info='消息标题')
    messageText = db.Column(db.String, info='消息内容')
    classID = db.Column(db.String(20), info='所属班级')
    recevierType = db.Column(db.String(20), info='接收人类型')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除1-删除')
    CreateTime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

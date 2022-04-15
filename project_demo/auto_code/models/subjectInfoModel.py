# coding: utf-8
from . import db


class SubjectInfo(db.Model):
    __tablename__ = 'subject_info'
    SubjectID = db.Column(db.String(20, 'utf8_general_ci'), primary_key=True, info='学科ID')
    SubjectName = db.Column(db.String(255), info='学科名称')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

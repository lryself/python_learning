# coding: utf-8
from . import db


class SchoolInfo(db.Model):
    __tablename__ = 'school_info'
    UniversityID = db.Column(db.Integer, primary_key=True, info='学校编号')
    UniversityName = db.Column(db.String(255, 'utf8_general_ci'), nullable=False, server_default=db.FetchedValue(), info='学校名称')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

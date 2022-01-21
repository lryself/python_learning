# coding: utf-8
from . import db


class ClassApply(db.Model):
    __tablename__ = 'class_apply'
    AutoID = db.Column(db.BigInteger, primary_key=True, info='自动编号')
    ClassID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='班级编号')
    StudentID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='学生ID')
    Status = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='申请状态:\\r\\n0-退课未处理\\r\\n1-退课已处理')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除，1-删除')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

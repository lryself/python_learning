# coding: utf-8
from . import db


class ClassStudent(db.Model):
    __tablename__ = 'class_student'
    AutoID = db.Column(db.BigInteger, primary_key=True, info='自动编号')
    ClassID = db.Column(db.String(20), nullable=False, info='班级编号')
    StudentID = db.Column(db.String(20), nullable=False, info='学生编号')
    StudentType = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='学生类型：\\r\\n0-普通学生\\r\\n1-旁听生')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除，1-删除')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

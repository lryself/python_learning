# coding: utf-8
from . import db


class ClassInfo(db.Model):
    __tablename__ = 'class_info'
    AutoID = db.Column(db.BigInteger, primary_key=True, info='自动编号')
    ClassID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, index=True, server_default=db.FetchedValue(), info='班级id')
    SubjectID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='学科ID')
    ClassName = db.Column(db.String(255, 'utf8_general_ci'), nullable=False, info='班级名称')
    TeacherID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='老师id')
    UniversityID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='所属学校')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除，1-删除')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

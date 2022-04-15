# coding: utf-8
from . import db


class ClassAccount(db.Model):
    __tablename__ = 'class_account'
    AutoID = db.Column(db.BigInteger, primary_key=True, info='自动编号')
    ClassID = db.Column(db.ForeignKey('class_info.ClassID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, server_default=db.FetchedValue(), info='班级id')
    QuestionAccountID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, index=True, info='问题批次（这属于哪一次的作业）')
    QuestionAccountName = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='问题编号')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除，1-删除')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    class_info = db.relationship('ClassInfo', primaryjoin='ClassAccount.ClassID == ClassInfo.ClassID', backref='class_accounts')

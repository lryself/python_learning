# coding: utf-8
from . import db


class QuestionInfo(db.Model):
    __tablename__ = 'question_info'
    QuestionID = db.Column(db.String(20, 'utf8_general_ci'), primary_key=True, info='问题编号')
    SubjectID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='学科ID')
    QuestionText = db.Column(db.String(collation='utf8_general_ci'), nullable=False, info='问题内容')
    AnswerText = db.Column(db.String, nullable=False, info='答案内容')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

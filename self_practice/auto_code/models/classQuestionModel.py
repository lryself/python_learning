# coding: utf-8
from . import db


class ClassQuestion(db.Model):
    __tablename__ = 'class_question'
    AutoID = db.Column(db.BigInteger, primary_key=True, info='自动编号')
    ClassID = db.Column(db.ForeignKey('class_info.ClassID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, info='班级编号')
    QuestionID = db.Column(db.ForeignKey('question_info.QuestionID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, info='问题编号')
    QuestionAccountID = db.Column(db.ForeignKey('class_account.QuestionAccountID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, info='问题批次（这属于哪一次的作业）')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除，1-删除')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    class_info = db.relationship('ClassInfo', primaryjoin='ClassQuestion.ClassID == ClassInfo.ClassID', backref='class_questions')
    class_account = db.relationship('ClassAccount', primaryjoin='ClassQuestion.QuestionAccountID == ClassAccount.QuestionAccountID', backref='class_questions')
    question_info = db.relationship('QuestionInfo', primaryjoin='ClassQuestion.QuestionID == QuestionInfo.QuestionID', backref='class_questions')

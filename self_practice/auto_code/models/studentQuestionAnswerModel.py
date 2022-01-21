# coding: utf-8
from . import db


class StudentQuestionAnswer(db.Model):
    __tablename__ = 'student_question_answer'
    AutoID = db.Column(db.BigInteger, primary_key=True, info='自动编号')
    StudentID = db.Column(db.String(20), nullable=False, info='学生编号')
    QuestionID = db.Column(db.String(20), nullable=False, info='问题编号')
    QuestionAccountID = db.Column(db.String(20), nullable=False, info='问题批次')
    AnswerText = db.Column(db.String, info='学生答案')
    IsReCheck = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未复议\\r\\n1-申请复议，待老师处理\\r\\n2-复议完成，老师已处理')
    ImageUrl = db.Column(db.String(255, 'utf8_general_ci'), nullable=False, info='图片储存路径')
    Grade = db.Column(db.Integer, info='成绩')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除，1-删除')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

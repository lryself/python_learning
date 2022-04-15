# coding: utf-8
from . import db


class UserInfo(db.Model):
    __tablename__ = 'user_info'
    __table_args__ = (
        db.Index('NonClusteredIndex-学生基本信息索引', 'UserID', 'UserName', 'UniversityID'),
    )
    UserID = db.Column(db.String(30, 'utf8_general_ci'), primary_key=True, info='编号id')
    UserName = db.Column(db.String(30, 'utf8_general_ci'), nullable=False, info='姓名')
    UserNumber = db.Column(db.String(30, 'utf8_general_ci'), info='学号、员工号、教工号')
    Password = db.Column(db.String(255, 'utf8_general_ci'), nullable=False, info='密码')
    Email = db.Column(db.String(255, 'utf8_general_ci'), nullable=False, info='邮箱')
    UniversityID = db.Column(db.String(20, 'utf8_general_ci'), info='学校')
    UserType = db.Column(db.String(10), nullable=False, info='用户类型\\r\\n1--学生\\r\\n2--老师\\r\\n3--学校管理员\\r\\n4--平台管理员')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

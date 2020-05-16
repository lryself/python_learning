# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, MetaData, String
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata



class Clas(Base):
    __tablename__ = 'class'

    id = Column(Integer, primary_key=True, info='课程编号')
    name = Column(String(255, 'utf8_general_ci'), server_default=FetchedValue(), info='课程名称')
    teacher = Column(String(255, 'utf8_general_ci'), server_default=FetchedValue(), info='课程教师')
    time = Column(String(11, 'utf8_general_ci'), server_default=FetchedValue(), info='上课时间')
    begin_week = Column(Integer, server_default=FetchedValue(), info='起始周数')
    end_week = Column(Integer, server_default=FetchedValue(), info='结束周数')



class StuChoose(Base):
    __tablename__ = 'stu_choose'

    id = Column(Integer, primary_key=True, info='序号')
    user = Column(ForeignKey('users.name', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, info='学生id')
    class_id = Column(ForeignKey('class.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, info='课程id')

    _class = relationship('Clas', primaryjoin='StuChoose.class_id == Clas.id', backref='stu_chooses')
    user1 = relationship('User', primaryjoin='StuChoose.user == User.name', backref='stu_chooses')



class User(Base):
    __tablename__ = 'users'

    name = Column(String(20, 'utf8_general_ci'), primary_key=True, info='用户名')
    password = Column(String(32, 'utf8_general_ci'), info='密码')
    is_student = Column(Integer, nullable=False, server_default=FetchedValue(), info='1为学生账号，0为管理员账号')

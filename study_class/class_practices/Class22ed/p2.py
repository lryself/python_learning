# -*- encoding: utf-8 -*-
"""
@File : p2
@Time : 2020/5/8 9:46
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
"""
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# here put the import lib
Base = declarative_base()


class Student(Base):
    # 表的名字：
    __tablename__ = 'test'

    # 表的结构：
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接
engine = create_engine(
    "mysql+pymysql://rj1801lry:lry12345678@rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com:3306/python_learn")

DBSession = sessionmaker(bind=engine)

session = DBSession()

users = session.query(Student).all()

for u in users:
    print(u.id, u.name)

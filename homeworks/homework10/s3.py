# -*- encoding: utf-8 -*-
"""
@File : s3
@Time : 2020/5/8 15:45
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：对2中的表结构，用SQLAchemy模块来实现同样的操作；
"""
from sqlalchemy import Column, String, create_engine, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from datetime import datetime
# here put the import lib


def choose():
    '''
    页面初始化

    :Return:返回用户选择的操作
    '''
    os.system('cls')
    print("您可以进行如下数据库操作：")
    i = 0
    print("{}.退出".format(i))
    i += 1
    print("{}.增加留言信息".format(i))
    i += 1
    print("{}.删除留言信息".format(i))
    i += 1
    print("{}.修改留言信息".format(i))
    i += 1
    print("{}.查询留言信息".format(i))
    i += 1
    print("{}.输出全部留言".format(i))
    i += 1
    try:
        n = int(input("请输入您要进行的操作数："))
        if n < 0 or n >= i:
            raise Exception
        return n
    except Exception:
        print("您输入的操作数有误，请重新输入！")


def base(func):
    def base1(self,word="",value="",tp=0):
        try:
            res = func(self,word,value,tp)
            return res
        except Exception as e:
            print(e)
            print("操作执行失败！")
    return base1


class Message(declarative_base()):
    __tablename__ = 'guestbook'

    id = Column(Integer, primary_key=True)
    contents = Column(String(50))
    people = Column(String(10))
    time = Column(DateTime,default=datetime.now())
    is_delete = Column(Integer,default=0)

    @base
    def add(self,*args):
        session = DBSession()
        session.add(self)
        session.commit()
        session.close()

    @classmethod
    @base
    def find(cls, word, value, tp=0):
        session = DBSession()
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        if tp == 1:
            users = session.query(Message).all()
        if word == 'id':
            users = session.query(Message).filter(Message.id == int(value)).all()
        elif word == 'contents':
            users = session.query(Message).filter(Message.contents == value).all()
        elif word == 'people':
            users = session.query(Message).filter(Message.people == value).all()
        elif word == 'time':
            users = session.query(Message).filter(Message.time == value).all()
        elif word == 'is_delete':
            users = session.query(Message).filter(Message.is_delete == int(value)).all()
        session.close()
        return users

    @classmethod
    @base
    def delete(cls, value,*args):
        session = DBSession()
        message = session.query(Message).filter(Message.id == int(value)).first()
        message.is_delete=1
        session.commit()
        session.close()

    @classmethod
    @base
    def update(cls, word, value,m_id,*args):
        session = DBSession()
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        users = session.query(Message).filter(Message.id == int(m_id)).all()
        for i in users:
            if word == 'id':
                i.id = int(value)
            elif word == 'contents':
                i.contents = value
            elif word == 'people':
                i.people = value
            elif word == 'time':
                i.time = datetime.strptime(value, '%b-%d-%Y %H:%M:%S')
            elif word == 'is_delete':
                i.is_delete = int(value)
        session.commit()
        session.close()
        return users


if __name__ == '__main__':
    try:
        engine = create_engine(
            "mysql+pymysql://rj1801lry:lry12345678@rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com:3306/python_learn")
        DBSession = sessionmaker(bind=engine)
    except Exception as e:
        print(e)
        print("数据库连接失败！")
    else:
        while True:
            n = choose()
            if n == 0:
                break
            elif n == 1:
                contents = input("请输入留言：")
                people = input("请输入留言人：")
                Message(contents=contents, people=people).add()
            elif n == 2:
                m_id = input("请输入您要删除的留言id：")
                Message.delete(m_id)
            elif n == 3:
                m_id = input("请输入您要修改的留言id：")
                m_word = input("请输入您要修改的字段：")
                m_value = input("请输入您要修改的值：")
                Message.update(m_word,m_value,m_id)
            elif n == 4:
                m_word = input("请输入您要查询的字段：")
                m_value = input("请输入您要查询的值：")
                res = Message.find(m_word, m_value)
                if len(res)==0:
                        print("查询结果为空！")
                else:
                    print(
                        "{:<5}{:50}{:>10}{:>30}".format(
                            "id", "contents", "people", "time"))
                    for i in res:
                        print(
                            "{:<5}{:50}{:>10}{:>30}".format(
                                i.id, i.contents, i.people, i.time.strftime('%b-%d-%Y %H:%M:%S')))
            elif n == 5:
                res = Message.find(tp=1)
                if len(res)==0:
                        print("查询结果为空！")
                else:
                    print(
                        "{:<5}{:50}{:>10}{:>30}{:>10}".format(
                            "id",
                            "contents",
                            "people",
                            "time",
                            "is_delete"))
                    for i in res:
                        print(
                            "{:<5}{:50}{:>10}{:>30}{:>10}".format(
                                i.id, i.contents, i.people, i.time.strftime('%b-%d-%Y %H:%M:%S'), i.is_delete))

            input("按回车继续")

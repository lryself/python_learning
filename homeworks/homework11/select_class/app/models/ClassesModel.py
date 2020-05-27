# -*- encoding: utf-8 -*-
"""
@File : Classes
@Time : 2020/5/20 9:02
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
import config
from flask_login import UserMixin
# here put the import lib


class Classes(db.Model):
    '''
    课程表
    '''
    __tablename__ = 'class'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, info='课程编号')
    name = db.Column(db.String(255, 'utf8_general_ci'), server_default=db.FetchedValue(), info='课程名称')
    teacher = db.Column(db.String(255, 'utf8_general_ci'), server_default=db.FetchedValue(), info='课程教师')
    time = db.Column(db.String(255, 'utf8_general_ci'), server_default=db.FetchedValue(), info='上课时间')
    begin_week = db.Column(db.Integer, server_default=db.FetchedValue(), info='起始周数')
    end_week = db.Column(db.Integer, server_default=db.FetchedValue(), info='结束周数')

    def add(self, *args) -> bool:
        '''

        :return: True为成功，False为失败
        '''
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            print("添加执行失败！")
            return False

    @classmethod
    def find_class(cls, word='id', value='', *args):
        '''
        :param word: 查询字段，id：课程id,name：课程名称,teacher：课程教师,time：上课时间,all：全部课程
        :param value: 查询值
        :return: None为失败
        '''
        try:
            if word == 'id':
                res = db.session.query(Classes).filter(
                    Classes.id == int(value)).all()
            elif word == 'name':
                res = db.session.query(Classes).filter(
                    Classes.name == value).all()
            elif word == 'teacher':
                res = db.session.query(Classes).filter(
                    Classes.teacher == value).all()
            elif word == 'time':
                res = db.session.query(Classes).filter(
                    Classes.time == value).all()
            elif word == 'all':
                res = db.session.query(Classes).all()
            else:
                raise Exception
            return res
        except Exception as e:
            print(e)
            print("查询执行失败！")
            return None

    @classmethod
    def delete_class(cls, cls_id) -> bool:
        '''

        :param cls_id: 要删除的课程id
        :return: True为成功，False为失败
        '''
        try:
            classes = cls.find_class(value=cls_id)[0]
            db.session.delete(classes)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            print("删除执行失败！")
            return False

    @classmethod
    def update_class(cls, word, value, cls_id, *args) -> bool:
        '''

        :param word: 查询字段,name：课程名称,teacher：课程教师,time：上课时间
        :param value: 查询值
        :param cls_id: 要更新的课程id
        :return: True为成功，False为失败
        '''
        try:
            # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
            classes = cls.find_class(value=cls_id)[0]
            if word == 'name':
                classes.name = value
            elif word == 'teacher':
                classes.teacher = value
            elif word == 'time':
                classes.time = int(value)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            print("更新执行失败！")
            return False
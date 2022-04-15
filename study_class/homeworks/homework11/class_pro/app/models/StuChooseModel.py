# -*- encoding: utf-8 -*-
"""
@File : StuChooseModel
@Time : 2020/5/20 9:02
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
# here put the import lib


class StuChoose(db.Model):
    __tablename__ = 'stu_choose'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, info='序号')
    user = db.Column(db.ForeignKey('users.name', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, info='学生id')
    class_id = db.Column(db.ForeignKey('class.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, info='课程id')

    _class = db.relationship('Classes', primaryjoin='StuChoose.class_id == Classes.id', backref='stu_chooses1')
    user1 = db.relationship('User', primaryjoin='StuChoose.user == User.name', backref='stu_chooses2')

    def add(self, *args) -> bool:
        '''
        添加选课信息
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
    def find_id(cls, word='user', value='', *args):
        '''
        查找选课信息
        :param word: 查询字段，name：用户名，class:学生账号
        :param value: 查询值
        :return: None为失败
        '''
        try:
            if word == 'user':
                res = db.session.query(cls).filter(cls.user == value).all()
            elif word == 'class_id':
                res = db.session.query(cls).filter(cls.class_id == int(value)).all()
            else:
                raise Exception
            return res
        except Exception as e:
            print(e)
            print("查询执行失败！")
            return None

    @classmethod
    def delete_class(cls, user, cls_id) -> bool:
        '''

        :param cls_id: 课程编号
        :param user: 用户编号
        :return: True为成功，False为失败
        '''
        try:
            res = db.session.query(StuChoose).filter(
                StuChoose.user == user, StuChoose.class_id == cls_id).first()
            db.session.delete(res)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            print("删除执行失败！")
            return False
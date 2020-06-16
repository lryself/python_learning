# -*- encoding: utf-8 -*-
"""
@File : UserModel
@Time : 2020/5/20 9:01
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
import config
# here put the import lib


class User(db.Model):
    '''
    用户表
    '''
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(20), primary_key=True, info='用户名')
    password = db.Column(db.String(255), info='密码')
    is_student = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1为学生账号，0为管理员账号')

    def add(self,*args) -> bool:
        '''
        添加账号
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
    def find_stu(cls,word='name', value='', *args):
        '''
        查找账号
        :param word: 查询字段，name：用户名，is_student:学生账号
        :param value: 查询值
        :return: None为失败
        '''
        try:
            if word == 'name':
                res = db.session.query(User).filter(User.name == value).all()[0]
            elif word == 'is_student':
                res = db.session.query(User).filter(User.is_student == int(value)).all()
            else:
                raise Exception
            return res
        except Exception as e:
            print(e)
            print("查询执行失败！")
            return None

    @classmethod
    def delete_stu(cls,user_name , user_password) -> bool:
        '''
        删除账号
        :param user_password: 用户密码
        :param user_name: 要删除的账号用户名
        :return: True为成功，False为失败
        '''
        try:
            user = cls.find_stu(value=user_name)[0]
            if user.password == user_password:
                db.session.delete(user)
            else:
                return False
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            print("删除执行失败！")
            return False

    @classmethod
    def update_stu(cls,stu_name, old_password, new_password, *args) -> bool:
        '''
        更新账号密码
        :param stu_name: 用户名
        :param old_password: 旧密码
        :param new_password: 新密码
        :return: True为成功，False为失败
        '''
        try:
            # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
            user = cls.find_stu(value=stu_name)[0]
            if user.password == old_password:
                user.password = new_password
            else:
                return False
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            print("更新执行失败！")
            return False

    @classmethod
    def is_true_user(cls, name, password):
        try:
            user = cls.find_stu(value=name)
            return check_password_hash(user.password, password)
        except Exception as e:
            print(e)
            print("判断执行失败！")
            return False

    @classmethod
    def is_stu(cls, name):
        try:
            res = cls.find_stu(value=name)
            if res.is_student == config.IS_STUDENT:
                return config.IS_STUDENT
            else:
                return config.IS_NOT_STUDENT
        except Exception as e:
            print(e)
            print("判断执行失败！")
            return None

    def set_password(self, password):
        self.password = generate_password_hash(password)

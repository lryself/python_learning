# coding: utf-8
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


class User(UserMixin, db.Model):
    '''
    用户表
    '''
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(20), primary_key=True, info='用户名')
    password = db.Column(db.String(32), info='密码')
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
            if password == user.password:
                return True
            else:
                return False
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

    def check_password(self, password):
        return check_password_hash(self.password, password)
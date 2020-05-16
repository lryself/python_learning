# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config

# here put the import lib


def db_load(user):
    '''
    登录数据库
    :param user:用户类型
    :return: DBSession
    '''
    try:
        if user == config.IS_STUDENT:
            engine = create_engine(
                "mysql+pymysql://{user}:{password}@{dburl}:3306/python_learn_selectclass".format(
                    user=config.DATABASE_STUDENT_USER,
                    password=config.DATABASE_STUDENT_PASSWARD,
                    dburl=config.DATABASE_URL))
        else:
            engine = create_engine(
                "mysql+pymysql://{user}:{password}@{dburl}:3306/python_learn_selectclass".format(
                    user=config.DATABASE_TEACHER_USER,
                    password=config.DATABASE_TEACHER_PASSWARD,
                    dburl=config.DATABASE_URL))
        return sessionmaker(bind=engine)
    except Exception as e:
        print(e)
        print("数据库连接失败！")


Base = declarative_base()
metadata = Base.metadata


class Classes(Base):
    '''
    课程表
    '''
    __tablename__ = 'class'

    id = Column(Integer, primary_key=True, info='课程编号')
    name = Column(String(255, 'utf8_general_ci'), server_default=FetchedValue(), info='课程名称')
    teacher = Column(String(255, 'utf8_general_ci'), server_default=FetchedValue(), info='课程教师')
    time = Column(String(255, 'utf8_general_ci'), server_default=FetchedValue(), info='上课时间')
    begin_week = Column(Integer, server_default=FetchedValue(), info='起始周数')
    end_week = Column(Integer, server_default=FetchedValue(), info='结束周数')

    def add(self, DBSession, *args) -> bool:
        '''

        :param DBSession:
        :return: True为成功，False为失败
        '''
        try:
            session = DBSession()
            session.add(self)
            session.commit()
            session.close()
            return True
        except Exception as e:
            print(e)
            print("添加执行失败！")
            return False

    @classmethod
    def find_class(cls, DBSession, word='id', value='', *args):
        '''

        :param DBSession:
        :param word: 查询字段，id：课程id,name：课程名称,teacher：课程教师,time：上课时间,all：全部课程
        :param value: 查询值
        :return: None为失败
        '''
        try:
            session = DBSession()
            # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
            if word == 'id':
                res = session.query(Classes).filter(
                    Classes.id == int(value)).all()
            elif word == 'name':
                res = session.query(Classes).filter(
                    Classes.name == value).all()
            elif word == 'teacher':
                res = session.query(Classes).filter(
                    Classes.teacher == value).all()
            elif word == 'time':
                res = session.query(Classes).filter(
                    Classes.time == value).all()
            elif word == 'all':
                res = session.query(Classes).all()
            else:
                raise Exception
            session.close()
            return res
        except Exception as e:
            print(e)
            print("查询执行失败！")
            return None

    @classmethod
    def delete_class(cls, DBSession, cls_id) -> bool:
        '''

        :param DBSession:
        :param cls_id: 要删除的课程id
        :return: True为成功，False为失败
        '''
        try:
            session = DBSession()
            classes = cls.find_class(DBSession, value=cls_id)[0]
            session.delete(classes)
            session.commit()
            session.close()
            return True
        except Exception as e:
            print(e)
            print("删除执行失败！")
            return False

    @classmethod
    def update_class(cls, DBSession, word, value, cls_id, *args) -> bool:
        '''

        :param DBSession:
        :param word: 查询字段,name：课程名称,teacher：课程教师,time：上课时间
        :param value: 查询值
        :param cls_id: 要更新的课程id
        :return: True为成功，False为失败
        '''
        try:
            session = DBSession()
            # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
            classes = cls.find_class(DBSession, value=cls_id)[0]
            if word == 'name':
                classes.name = value
            elif word == 'teacher':
                classes.teacher = value
            elif word == 'time':
                classes.time = int(value)
            session.commit()
            session.close()
            return True
        except Exception as e:
            print(e)
            print("更新执行失败！")
            return False


class StuChoose(Base):
    __tablename__ = 'stu_choose'

    id = Column(Integer, primary_key=True, info='序号')
    user = Column(ForeignKey('users.name', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, info='学生id')
    class_id = Column(ForeignKey('class.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, info='课程id')

    _class = relationship('Classes', primaryjoin='StuChoose.class_id == Classes.id', backref='stu_chooses')
    user1 = relationship('User', primaryjoin='StuChoose.user == User.name', backref='stu_chooses')

    def add(self, DBSession, *args) -> bool:
        '''
        添加选课信息
        :param DBSession:
        :return: True为成功，False为失败
        '''
        try:
            session = DBSession()
            res = session.query(StuChoose).filter(
                StuChoose.user == self.user,
                StuChoose.class_id == self.class_id).first()
            if res:
                session.add(self)
            else:
                return False
            session.commit()
            session.close()
            return True
        except Exception as e:
            print(e)
            print("添加执行失败！")
            return False

    @classmethod
    def find_id(cls, DBSession, word='user', value='', *args):
        '''
        查找选课信息
        :param DBSession:
        :param word: 查询字段，name：用户名，class:学生账号
        :param value: 查询值
        :return: None为失败
        '''
        try:
            session = DBSession()
            if word == 'user':
                res = session.query(StuChoose).filter(StuChoose.user == value).all()
            elif word == 'class_id':
                res = session.query(StuChoose).filter(StuChoose.class_id == int(value)).all()
            else:
                raise Exception
            session.close()
            return res
        except Exception as e:
            print(e)
            print("查询执行失败！")
            return None

    @classmethod
    def delete_class(cls, DBSession, user, cls_id) -> bool:
        '''

        :param cls_id: 课程编号
        :param user: 用户编号
        :param DBSession:
        :return: True为成功，False为失败
        '''
        try:
            session = DBSession()
            res = session.query(StuChoose).filter(
                StuChoose.user == user, StuChoose.class_id == cls_id).first()
            session.delete(res)
            session.commit()
            session.close()
            return True
        except Exception as e:
            print(e)
            print("删除执行失败！")
            return False


class User(Base):
    '''
    用户表
    '''
    __tablename__ = 'users'

    name = Column(String(20), primary_key=True, info='用户名')
    password = Column(String(32), info='密码')
    is_student = Column(Integer, nullable=False, server_default=FetchedValue(), info='1为学生账号，0为管理员账号')

    def add(self, DBSession, *args) -> bool:
        '''
        添加账号
        :param DBSession:
        :return: True为成功，False为失败
        '''
        try:
            session = DBSession()
            session.add(self)
            session.commit()
            session.close()
            return True
        except Exception as e:
            print(e)
            print("添加执行失败！")
            return False

    @classmethod
    def find_stu(cls, DBSession, word='name', value='', *args):
        '''
        查找账号
        :param DBSession:
        :param word: 查询字段，name：用户名，is_student:学生账号
        :param value: 查询值
        :return: None为失败
        '''
        try:
            session = DBSession()
            # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
            if word == 'name':
                res = session.query(User).filter(User.name == value).all()
            elif word == 'is_student':
                res = session.query(User).filter(User.is_student == int(value)).all()
            else:
                raise Exception
            session.close()
            return res
        except Exception as e:
            print(e)
            print("查询执行失败！")
            return None

    @classmethod
    def delete_stu(cls, DBSession, user_name, user_password) -> bool:
        '''
        删除账号
        :param user_password: 用户密码
        :param DBSession:
        :param user_name: 要删除的账号用户名
        :return: True为成功，False为失败
        '''
        try:
            session = DBSession()
            user = cls.find_stu(DBSession, value=user_name)[0]
            if user.password == user_password:
                session.delete(user)
            else:
                return False
            session.commit()
            session.close()
            return True
        except Exception as e:
            print(e)
            print("删除执行失败！")
            return False

    @classmethod
    def update_stu(cls, DBSession, stu_name, old_password, new_password, *args) -> bool:
        '''
        更新账号密码
        :param DBSession:
        :param stu_name: 用户名
        :param old_password: 旧密码
        :param new_password: 新密码
        :return: True为成功，False为失败
        '''
        try:
            session = DBSession()
            # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
            user = cls.find_stu(DBSession, value=stu_name)[0]
            if user.password == old_password:
                user.password = new_password
            else:
                return False
            session.commit()
            session.close()
            return True
        except Exception as e:
            print(e)
            print("更新执行失败！")
            return False

    @classmethod
    def is_true_user(cls, DBSession, name, password):
        try:
            user = cls.find_stu(DBSession, value=name)[0]
            if password == user.password:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            print("判断执行失败！")
            return False

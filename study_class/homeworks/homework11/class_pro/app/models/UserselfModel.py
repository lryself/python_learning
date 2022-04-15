# -*- encoding: utf-8 -*-
"""
@File : User
@Time : 2020/5/16 18:59
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from flask_login._compat import text_type
from config import IS_STUDENT
from app import login_manager
from models import UserModel, StuChooseModel, ClassesModel
from flask_login import UserMixin

# here put the import lib


def end_update(func):
    def end_update1(*args, **kwargs):
        res = func(*args, **kwargs)
        # Userself.load_class_times(args[0])
        load_user(args[0].username)
        return res

    return end_update1


def authentication(func):
    def aut1(*args, **kwargs):
        if args[0].is_student != IS_STUDENT:
            res = func(*args, **kwargs)
            return res
        else:
            return None

    return aut1


class Userself(UserMixin):  #继承flask_login的UserMixin
    def __init__(self, name):
        self.class_times = [[[0 for cls in range(10)] for col in range(7)] for row in range(25)] #现有课程的时间[周数][天数][节数]
        self.username = name #用户名
        self.password = UserModel.User.find_stu(value=name).password #用户密码
        self.is_student = UserModel.User.is_stu(name) #用户权限
        self.classes=[] #已报课程
        self.load_class_times(self)

    def get_id(self):
        return text_type(self.username)

    @staticmethod
    def load(username, password) -> bool:
        '''
        用户登录验证
        :param username: 用户名
        :param password: 密码
        :return: 登录结果
        '''
        if UserModel.User.is_true_user(name=username, password=password):
            print("登录成功！")
            return True
        else:
            print("登录失败！")
            return False

    @staticmethod
    def load_class_times(self):
        '''
        用于将学生已经选的课加载进学生信息中
        :return:
        '''
        self.class_times = [[[0 for cls in range(10)] for col in range(7)] for row in range(25)]
        res = StuChooseModel.StuChoose.find_id(word='user', value=self.username)
        if res:
            for i in res:
                self.classes.append(i.class_id)
                cls = ClassesModel.Classes.find_class(word='id', value=i.class_id)[0]
                cls_times = cls.time.split('|')
                for j in range(cls.begin_week - 1, cls.end_week):
                    for w in cls_times:
                        week, num = w.split('_')
                        self.class_times[j][int(week) - 1][int(num) - 1] = i.class_id
        else:
            print("加载失败！")

    @end_update
    def add_class(self, class_id):
        '''
        添加选课信息
        :param class_id: 课程编号
        :return: 选课结果
        '''
        if class_id in self.classes:
            return False
        newclass = StuChooseModel.StuChoose()
        newclass.user = self.username
        newclass.class_id = class_id
        newclass_res = ClassesModel.Classes.find_class(word='id', value=class_id)[0]

        # 判断是否与已选课程冲突
        if newclass_res:
            cls_times = newclass_res.time.split('|')
            for j in range(newclass_res.begin_week - 1, newclass_res.end_week):
                for w in cls_times:
                    week, num = w.split('_')
                    if self.class_times[j][int(week) - 1][int(num) - 1] != 0:
                        return False
        else:
            return False
        res = newclass.add()
        return res

    @end_update
    def del_class(self, class_id: int) -> bool:
        '''
        删除选课信息
        :param class_id: 课程id
        :return: 删除结果
        '''
        res = StuChooseModel.StuChoose.delete_class(cls_id=class_id, user=self.username)
        return res

    def upd_password(self, oldpassword: str, newpassword: str) -> bool:
        '''
        修改密码
        :param oldpassword: 旧密码
        :param newpassword: 新密码
        :return: 修改结果
        '''
        res = UserModel.User.update_stu(
            stu_name=self.username,
            old_password=oldpassword,
            new_password=newpassword)
        return res

    def find_allclass(self):
        res = StuChooseModel.StuChoose.find_id(word='user', value=self.username)
        if res:
            return res
        else:
            return None

    @authentication
    def additive_class(
        self, class_name: str, class_teacher: str, class_time: str, class_begin_week: int, class_end_week: int):
        '''
        管理员创建课程
        :param class_name: 课程名称
        :param class_teacher: 课程教师
        :param class_time: 课程时间
        :param class_begin_week: 课程开始周数
        :param class_end_week: 课程结束周数
        :return: bool 添加结果
        '''
        cls = ClassesModel.Classes()
        cls.name = class_name
        cls.teacher = class_teacher
        cls.time = class_time
        cls.begin_week = class_begin_week
        cls.end_week = class_end_week
        res = cls.add()
        return res

    @authentication
    def delete_class(self, class_id: str) -> bool:
        '''
        管理员删除课程信息
        :param class_id: 课程id
        :return: 删除结果
        '''
        res = ClassesModel.Classes.delete_class(cls_id=class_id)
        return res

    @authentication
    def update_class(self, *args):
        '''
        管理员修改课程信息
        :param args:
        :return: 修改结果
        '''
        res = ClassesModel.Classes.update_class(*args)
        return res

    @authentication
    def additive_user(self, username, password, is_student):
        user = UserModel.User()
        user.name = username
        user.password = password
        user.is_student = is_student
        return user.add()

    @authentication
    def delete_user(self, username):
        return UserModel.User.delete_stu(username)


@login_manager.user_loader
def load_user(user_id):
    user = Userself(user_id)
    return user

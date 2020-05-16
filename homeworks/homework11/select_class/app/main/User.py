# -*- encoding: utf-8 -*-
"""
@File : User
@Time : 2020/5/16 18:59
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from config import IS_STUDENT
import tools
import db_option
# here put the import lib

class Userself():
    def __init__(self, name, password, is_student):
        self.class_times = [[[0 for cls in range(10)] for col in range(7)] for row in range(25)]
        self.username = name
        self.password = password
        self.is_true_user = False
        self.is_student = is_student
        self.DBSession = db_option.db_load(self.is_student)

    def load(self):
        if db_option.User.is_true_user(DBSession=self.DBSession, name=self.username, password=self.password):
            print("登录成功！")
            return True
        else:
            print("登录失败！")
            return False

    def load_class_times(self):
        res=db_option.StuChoose.find_id(DBSession=self.DBSession, word='user', value=self.username)
        if res:
            for i in res:
                cls=db_option.Classes.find_class(DBSession=self.DBSession,word='id',value=i.class_id)[0]
                cls_times=cls.time.split('|')
                for j in range(cls.begin_week-1,cls.end_week):
                    for w in cls_times:
                        week,num=w.split('_')
                        self.class_times[j][int(week)-1][int(num)-1]=i.class_id
        else:
            print("加载失败！")

if __name__ == '__main__':
    temp=Userself('stu1','123456',1)
    temp.load_class_times()
    print(temp.class_times)
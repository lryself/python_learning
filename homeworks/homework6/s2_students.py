# -*- encoding: utf-8 -*-
'''
@File : s2.py
@Time : 2020/04/09 08:51:44
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：定义一个学生Student类。有下面的类属性：
1 姓名 name
2 年龄 age
3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:
'''

# here put the import lib
class Student(object):

    def __init__(self,name="",age=0,score_Chinese=0,score_math=0,score_English=0):
        self.__name=name
        self.__age=age
        self.__score={}
        self.__score["语文"]=score_Chinese
        self.__score["数学"]=score_math
        self.__score["英语"]=score_English

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age

    def get_course(self):
        return max(self.__score.values())

if __name__ == "__main__":
    stu1=Student("Tom",18,78,80,92)
    stu2=Student("Sam",20,69,89,83)

    print(stu1.getname())
    print(stu1.get_course())
    print(stu2.get_course())
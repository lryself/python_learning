# -*- encoding: utf-8 -*-
'''
@File : s4_student.py
@Time : 2020/04/09 12:57:55
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
      封装方法，求单个学生的总分，平均分，以及打印学生的信息。
'''

# here put the import lib

class Student4():
      def __init__(self,name="",age=0,sex="男",score_Chinese=0,score_math=0,score_English=0):
            self.__name=name
            self.__age=age
            self.__sex=sex
            self.__score={}
            self.__score["语文"]=score_Chinese
            self.__score["数学"]=score_math
            self.__score["英语"]=score_English

      def sum_score(self):
            return sum(self.__score.values())

      def average_score(self):
            return sum(self.__score.values())/len(self.__score.values())

      def print_data(self):
            print("学生姓名：{}，年龄:{}，性别：{}，英语成绩：{}，数学成绩：{}，语文成绩：{}".format(self.__name,self.__age,self.__sex,self.__score["英语"],self.__score["数学"],self.__score["语文"]))
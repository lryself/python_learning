# -*- encoding: utf-8 -*-
'''
@File : s6_stuscore.py
@Time : 2020/04/09 14:44:43
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：用面向对象,实现一个学生Python成绩管理系统;
      学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
      实现对学生信息及成绩的增,删,改,查方法;
'''

# here put the import lib
class student(object):
    def __init__(self,data):
        self.class1=data[0]
        self.num=data[1]
        self.name=data[2]
        self.score=data[3]
    
    def print_data(self):
        print("班级：{} 姓名：{} 学号：{} python成绩：{}".format(self.class1,self.num,self.name,self.score))

class stu_score(object):
    def __init__(self,f):
        self.stu=[]
        try:
            with open(f,"r") as f1:
                data=f1.readlines()
                for i in data:
                    data1=i.strip().split()
                    self.stu.append(student(data1))
        except EOFError:
            print("没有找到文件")

    def addstu(self,newstu):
        self.stu.append(newstu)
    
    def delstu(self,stuname):
        self.stu.remove(self.findstu(stuname))
    
    def findstu(self,stuname):
        for i in self.stu:
            if i.name==stuname:
                return i
    def changestu(self,stuname,stuscore):
        self.findstu(stuname).score=stuscore

if __name__ == "__main__":
    # f=input("请输入学生信息的文件的绝对路径:")
    f="F:\programme\GitHub\python_learning\homeworks\homework6\student.txt"
    data=stu_score(f)
    while True:
        print("0.退出程序")
        print("1.增加学生")
        print("2.删除学生")
        print("3.修改学生成绩")
        print("4.查找学生成绩")
        print("5.输出信息")
        choose=int(input("请输入你要进行的操作序号："))
        if choose==0:
            break
        elif choose==1:
            stu1=student(list(input("请输入学生的班级,学号,姓名, Python成绩，用空格隔开:\n").split()))
            data.addstu(stu1)
        elif choose==2:
            stu1=input("请输入学生的姓名:\n")
            data.delstu(stu1)
        elif choose==3:
            stu1=list(input("请输入学生的姓名和成绩，用空格隔开:\n").split())
            data.changestu(stu1[0],int(stu1[1]))
        elif choose==4:
            stu1=input("请输入学生的姓名:\n")
            if data.findstu(stu1):
                data.findstu(stu1).print_data()
        elif choose==5:
            with open(f,"w") as f1:
                for i in data.stu:
                    f1.write("{} {} {} {}\n".format(i.class1,i.name,i.num,i.score))
        else:
            print("输入错误，请重新输入")
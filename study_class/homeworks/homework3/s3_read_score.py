# -*- encoding: utf-8 -*-
'''
@File : s3_read_score.py
@Time : 2020/03/20 19:38:21
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出
'''
import tools
# here put the import lib
stus=[]
try:
    with open("student_score.txt", "r") as f:
        stus=f.readlines()
except OSError:
    print("文件打开失败，当前工作目录为：",os.getcwd)
else:
    for i in range(len(stus)):
        stus[i]=tuple(stus[i].strip("\n").split(","))
    stus=sorted(stus,key=lambda s: s[2],reverse=True)
    for i in stus:
        print(i)
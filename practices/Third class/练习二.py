# -*- encoding: utf-8 -*-
'''
@File : 练习二.py
@Time : 2020/02/28 21:20:48
@Author : lryself 
@Version : 1.0
@Contact : lryself@163.com
'''

# here put the import lib

'''题目：定义一个字符串,分别进行查找某个字符串是否包含在这个字符串里面; 进行某个字符串的替换; 打印字符串的长度;
'''
str1="Hallo World"
str2="Hallo"
print(str1.find(str2))
print(str1.find("lry"))
print(len(str1))
print(str1.replace("World","Python_World"))

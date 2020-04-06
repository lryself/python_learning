# -*- encoding: utf-8 -*-
'''
@File : s3_password.py
@Time : 2020/04/06 18:23:58
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
'''

# here put the import lib
def load(func):
    def load1(*args):
        username=input("请输入您的用户名：")
        password=input("请输入您的密码：")
        res=func(*args)
        return res
    return load1

@load
def addition(*args):
    res=sum(args)
    return res

print(addition(1,2,3,4))
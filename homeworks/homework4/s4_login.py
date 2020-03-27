# -*- encoding: utf-8 -*-
'''
@File : s4_login.py
@Time : 2020/03/27 16:35:27
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：模拟用户登录:
     5个同学的姓名,账号和密码(加密后的),保存在一个文件上;
     系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;
     如果都正确,打印提示, 您登录成功(失败);
'''
import tools
import hashlib
# here put the import lib
alluser=[]
with open("user.txt","r",encoding="utf-8") as f:
    alluser=f.readlines()

for i in range(len(alluser)):
    alluser[i]=alluser[i].strip().split(",")

flag=True
user=[]

username=input("请输入登录同学的姓名：")
for i in alluser:
    if i.count(username)==1:
        user=i
        break
else:
    flag=False
if flag:
    userid=input("请输入账号：")
    if user[1]!=userid:
        flag=False
if flag:
    md5=hashlib.md5()
    md5.update(input("请输入密码：").encode("utf-8"))
    userpassword=md5.hexdigest()
    if user[2]!=userpassword:
        flag=False
if flag:
    print("登录成功！")
else:
    print("登陆失败！")
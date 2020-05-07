# -*- encoding: utf-8 -*-
'''
@File : p1_mysql-connector.py
@Time : 2020/05/07 09:14:18
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：自己练习
'''
import mysql.connector
# here put the import lib
mydb = mysql.connector.connect(
  host="rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com",       # 数据库主机地址
  user="lryself",    # 数据库用户名
  passwd="lpc123LPC",   # 数据库密码
)
mycursor = mydb.cursor()
 
mycursor.execute("SHOW DATABASES")
 
for x in mycursor:
  print(x)
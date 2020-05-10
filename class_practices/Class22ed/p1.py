# -*- encoding: utf-8 -*-
'''
@File : p1.py
@Time : 2020/05/08 07:54:34
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
'''
import pymysql
import tools
import random
# here put the import lib
db=pymysql.connect("rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com","lryself","lpc123LPC","python_learn")

cursor=db.cursor()
name=tools.random_name()
age=random.randint(5,30)
sql="""insert into user(name,age)
        value(name,age)
    """
try:
    #执行SQL语句
    cursor.execute(sql)

    #提交数据库
    db.commit()

    print("插入记录成功！")
except Exception as e:
    print(e)
finally:
    #关闭数据库
    db.close()
# -*- encoding: utf-8 -*-
"""
@File : config.py
@Time : 2020/5/13 8:45
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：sqlacodege的用法
"""
# here put the import lib
# sqlacodegen --outfile=models.py mysql://rj1801lry:lry12345678@rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com:3306/python_learn?charset=utf8 --tables guestbook

SQLALCHEMY_DATABASE_URL="mysql+pymysql://rj1801lry:lry12345678@rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com:3306/python_learn"

POOL_SIZE=5

MAX_OVERFLOW=4
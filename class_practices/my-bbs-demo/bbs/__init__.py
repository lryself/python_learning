# -*- encoding: utf-8 -*-
"""
@File : __init__.py
@Time : 2020/5/13 8:55
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# here put the import lib
try:
    engine = create_engine(
        "mysql+pymysql://rj1801lry:lry12345678@rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com:3306/python_learn")
    DBSession = sessionmaker(bind=engine)
except Exception as e:
    print(e)
    print("数据库连接失败！")
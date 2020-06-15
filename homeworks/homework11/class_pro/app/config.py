# -*- encoding: utf-8 -*-
"""
@File : config
@Time : 2020/6/14 22:47
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
# here put the import lib
import os
# here put the import lib
basedir = os.path.abspath(os.path.dirname(__file__))

# 数据库变量
DATABASE_URL = "rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com"
DATABASE_STUDENT_USER = "temp1"
DATABASE_STUDENT_PASSWARD = "Xx123456"
DATABASE_TEACHER_USER = "temp2"
DATABASE_TEACHER_PASSWARD = "Ll123456"
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/python_learn_selectclass?charset=utf8'.format(
    user=DATABASE_TEACHER_USER, password=DATABASE_TEACHER_PASSWARD, host=DATABASE_URL, port=3306)
SQLALCHEMY_TRACK_MODIFICATIONS = False
IS_STUDENT = 1
IS_NOT_STUDENT = 0

# 加载数据库文件
# flask-sqlacodegen --outfile=models.py mysql://temp2:Ll123456@"rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com":3306/python_learn_selectclass?charset=utf8--flask

# 导出第三方库
# pip freeze >requirements.txt

# 表单保护
CSRF_ENABLED = True
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
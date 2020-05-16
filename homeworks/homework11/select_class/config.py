# -*- encoding: utf-8 -*-
"""
@File : config
@Time : 2020/5/16 11:16
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
全局变量配置文件
"""
# here put the import lib

# 数据库变量
DATABASE_URL="rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com"
DATABASE_STUDENT_USER="temp1"
DATABASE_STUDENT_PASSWARD="Xx123456"
DATABASE_TEACHER_USER="temp2"
DATABASE_TEACHER_PASSWARD="Ll123456"
IS_STUDENT=1

# sqlacodegen --outfile=models.py mysql://temp2:Ll123456@"rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com":3306/python_learn_selectclass?charset=utf8 --tables stu_choose
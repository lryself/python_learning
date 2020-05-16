# -*- encoding: utf-8 -*-
"""
@File : manage
@Time : 2020/5/16 11:15
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：开发设计一个简单的基于web的选课系统（基于flask框架）；学生登陆后，能看到课程列表，点击可以选择该课程（要检查是否和其它已经选择的课程有时间冲突）；
    自己设计数据库，注意表和字段命名的规范性，数据类型选择的合理性；
文件内容：启动程序
"""
# here put the import lib
from app import create_app
from flask_script import Manager


app = create_app()
# manager = Manager(app)

# @app.route('/')
# def index():
#     return '首页'


if __name__ == '__main__':
    app.run(debug=True)
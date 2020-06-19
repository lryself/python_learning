# 大作业11---基于web的选课系统（基于flask框架）
---
## 1.引言
### **1.1题目要求**：
开发设计一个简单的基于web的选课系统（基于flask框架）；学生登陆后，能看到课程列表，点击可以选择该课程（要检查是否和其它已经选择的课程有时间冲突）；
    自己设计数据库，注意表和字段命名的规范性，数据类型选择的合理性；

### **1.2项目背景**：
* 本项目使用了flask框架完成web项目，使用了flask_wtf，flask_login等组件
* 本项目于2020年6月19日功能全部完成
* 本项目使用了mysql云数据库
## 2.总体设计
### 2.1 需求分析：
1. 项目目标：开发设计一个简单的选课系统
2. 项目功能：学生进行选课操作，管理员进行管理用户的操作
3. 项目分析：包含的功能有登录，登出，选课，退课，查看课程表，添加人员，删除人员，添加课程，删除课程等
### 2.2 开发机配置：
1. 处理器：intel 8th i5-8300H
2. 内存：8GB
3. 系统：windows 10 64位 
### 2.3 项目结构：
* app --项目主体
	* form --网页所需表单
	* model --数据库数据模型
	* static --网站生成的静态资源（图片，css，视频等）
	* templates --网页的html
	* views --网页视图
	* \_\_init__ --项目初始化
	* config.py --全局变量配置
	* test.py --功能测试
* venv --虚拟环境
* README.md --项目说明
* requirements.txt --所需第三方库
* run.py --项目运行入口
### 2.4 数据库设计：

![image](https://test-lry.oss-cn-beijing.aliyuncs.com/image/%E6%95%B0%E6%8D%AE%E5%BA%93%E5%9B%BE%E7%A4%BA.png?Expires=1592556705&OSSAccessKeyId=TMP.3KdjosWJhTmyZnJXm3zxfgzyf1S2SehfzGqsWniM3HUCJ6Xocim2xvQQMhhjrmEphs5jLzjdGaomRFoumJ6wLn5j3CXJLe&Signature=6VtqZfKq41EIXsAIumS12qlL6WM%3D)

* 数据库中共有3个表
	* class --所有的课程
		* id --课程编号
		* name --课程名称
		* teacher --课程教师
		* time --上课时间
		* begin_week --课程起始周数
		* end_week --课程结束周数
	* users --用户列表
		* name --用户名
		* password --用户密码
		* is_student --用户权限，1为学生，0为管理员
	* stu_choose --学生选择课程
		* id --主键
		* user --用户名 --外键连接user的用户名
		* class_id --课程编号 --外键连接class的课程编号

### 2.5 用户类Userself设计：
    class Userself(UserMixin):  #继承flask_login的UserMixin
    def __init__(self, name):
        self.class_times = [[[0 for cls in range(10)] for col in range(7)] for row in range(25)] #现有课程的时间[周数][天数][节数]
        self.username = name #用户名
        self.password = UserModel.User.find_stu(value=name).password #用户密码
        self.is_student = UserModel.User.is_stu(name) #用户权限
        self.classes=[] #已报课程
### 2.6 用户权限设计
* 学生账户：
	* 选择课程
	* 退选课程
	* 查看课程表
* 管理员账户：
	* 添加、删除用户
	* 添加、删除课程
### 2.7 需人工处理的步骤：
无
## 3.运行设计
1. 程序运行的入口为run.py
2. 程序提供两个初始账号
	1. 账号：stu1 密码：123456 --学生权限账号
	2. 账号：teacher1 密码：12345 --管理员权限账号
3. 学生账号可以进行自己课程的添加和删除操作，还可以查看自己的课程表
4. 老师账号可以对所有账号进行管理，对所有课程进行管理
## 4.不足
网页美工较差
## 备注：
1. 程序已调整符合pep8编码规范
2. 采用utf-8字符编码
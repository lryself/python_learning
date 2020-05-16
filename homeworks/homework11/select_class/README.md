# python综合大作业--学生选课系统
#### 题目要求：开发设计一个简单的基于web的选课系统（基于flask框架）；学生登陆后，能看到课程列表，点击可以选择该课程（要检查是否和其它已经选择的课程有时间冲突）；自己设计数据库，注意表和字段命名的规范性，数据类型选择的合理性；
## 项目结构
1. README.md  项目的介绍
2. manage.py  启动程序
3. requirements.txt  列出了所有依赖包以及版本号，方便在其他位置生成相同的虚拟环境以及依赖
4. venv  虚拟环境，python3.7.6
5. app  程序包
	1. templates jinjia2模板
	2. static css、js、图片等静态文件
	3. main  py程序包 ，可以有多个这种包，每个对应不同的功能
		1. __init__.py
		3. forms.py
		4. views.py
	4. __init__.py


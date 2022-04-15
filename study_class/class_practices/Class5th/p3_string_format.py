# -*- encoding: utf-8 -*-
'''
@File : 练习三.py
@Time : 2020/03/04 08:40:10
@Author : lryself 
@Version : 1.0
@Contact : lryself@163.com
'''

# here put the import lib
'''题目：将这4中方式实现的代码分别在vscode上练习一下; 观察输出结果
'''
username = input('username:')
password = input('password:')
print(username, password)

# name = input("name:") 
# age = input("age:") 
# skill = input("skill:") 
# salary = input("salary:") 
# info = ''' --- info of ''' + name + ''' name: ''' + name + ''' age: ''' + age + ''' skill: ''' + skill + ''' salary: ''' + salary + ''' ''' 
# print(info)

# name = input("name:") 
# age = input("age:") 
# skill = input("skill:") 
# salary = input("salary:") 
# info1 = ''' --- info of %s --- Name:%s Age:%s Skill:%s Salary:%s ''' % (name,name,age,skill,salary) 注意这里的变量要一 一对应，缺少一个就会报错 
# print(info1)

# name = input("username：") 
# age = input("age：") 
# skill = input("skill：") 
# salary = input("salary：") 
# info = ''' --- info of {_name} Name：{_name} Age：{_age} Skill：{_skill} Salary：{_salary} '''.format(_name=name, _age=age, _skill=skill, _salary=salary) //此处是赋值 
# print(info)

# name = input("name：") 
# age = input("age：") 
# skill = input("skill：") 
# salary = input("salary：") 
# info = ''' --- info of {0}--- Name：{0} Age：{1} Skill：{2} Salary：{3} '''.format(name, name, age, skill, salary) 
# print(info)

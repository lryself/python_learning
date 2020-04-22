# -*- encoding: utf-8 -*-
'''
@File : p1_count_tool.py
@Time : 2020/04/01 08:26:31
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：定义一个高阶函数, 实现加,减,乘,除计算器功能;
'''

# here put the import lib
def jsq(x, y, action):
    def jia(x, y):
        result = x + y
        return result

    def jian(x, y):
        result = x - y
        return result

    def chen(x, y):
        result = x * y
        return result

    def chu(x, y):
        result = x / y
        return result

    if action == '+':
        result = jia(x, y)
        print("{}+{}={}".format(x, y, result))
    elif action == '-':
        result = jian(x, y)
        print("{}-{}={}".format(x, y, result))
    elif action == '*':
        result = chen(x, y)
        print("{}*{}={}".format(x, y, result))
    elif action == '/':
        result = chu(x, y)
        print("{}/{}={}".format(x, y, result))
    else:
        print("暂时不支持这种操作")

if __name__ == "__main__":
    data=input("请输入你要计算的简单算式，数字和操作符之间用空格隔开").split()
    data[0]=int(data[0])
    data[2]=int(data[2])
    jsq(data[0],data[2],data[1])
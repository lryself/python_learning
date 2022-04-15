# -*- encoding: utf-8 -*-
'''
@File : s1.py
@Time : 2020/04/08 20:34:56
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
       实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
'''
import unittest
from random import randint
# here put the import lib

class dog(object):
    members=[]#狗的成员
    def __init__(self):
        a={"color":"white","number":20,"price":6000}
        b={"color":"black","number":30,"price":8000}
        c={"color":"pink","number":40,"price":10000}
        self.members=[a,b,c]

    def sold(self,color="",number=0):
        for i in self.members:
            if i["color"]==color:
                if number<=i["number"]:
                    i["number"]-=number
                    print("交易成功！您购买了{}只{}颜色的狗，总价为：{}".format(number,color,i["price"]*number))
                else:
                    print("交易失败！剩余狗的数量不足！")
                break
        else:
            print("您要购买的狗的颜色不存在")

    def printdog(self):
        print("现在剩余的狗有：")
        for i in self.members:
            print("{}颜色的狗{}只".format(i["color"],i["number"]))
        print()

if __name__ == "__main__":
    dog1=dog()
    dog1.sold("black",5)
    dog1.sold("white",3)
    dog1.sold("pink",12)
    dog1.printdog()
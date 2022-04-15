# -*- encoding: utf-8 -*-
'''
@File : p1_class.py
@Time : 2020/04/08 09:17:46
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：定义一个dog类(颜色, 名称), 里面有一个狗叫的方法; 不同的狗叫声可能不一样;  然后实例化几条狗, 然后统计实例化狗的数量
'''

# here put the import lib
class dog(object):
    name=""
    color=""
    __count=0
    def __init__(self,a,b):
        self.color=a
        self.name=b
        dog.__count+=1

    @classmethod
    def countdog(cls):
        return dog.__count
    
    def speak(self):
        print("{}狗在叫".format(self.name))


dog1=dog("a","g1")
dog2=dog("b","g2")
dog3=dog("c","g3")

print("一共有{0}条狗".format(dog.countdog()))
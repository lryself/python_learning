# -*- encoding: utf-8 -*-
'''
@File : s5_dog.py
@Time : 2020/04/09 22:19:49
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
'''

# here put the import lib
class Dog(object):
    def __init__(self):
        self.life=80
        self.atk=15

    def attack(self,enemy):
        if self.atk>0:
            enemy.life-=self.atk
            enemy.atk-=2
        if enemy.atk<=0:
            enemy.atk=0
        # print("狗攻击了人")
        if enemy.life <= 0:#判断死亡
            # print("一个人死亡")
            return enemy
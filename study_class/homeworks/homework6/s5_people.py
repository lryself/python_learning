# -*- encoding: utf-8 -*-
'''
@File : s5_people.py
@Time : 2020/04/09 22:20:16
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
'''

# here put the import lib
class People(object):
    def __init__(self):
        self.life=100
        self.atk=10
    
    def attack(self,enemy):
        if self.atk>0:
            enemy.life-=self.atk
            enemy.atk-=3
        if enemy.atk<=0:
            enemy.atk=0
        # print("人攻击了狗")
        if enemy.life <= 0:#判断死亡
            # print("一只狗死亡")
            return enemy
        return None
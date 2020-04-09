# -*- encoding: utf-8 -*-
'''
@File : s5_game_fight.py
@Time : 2020/04/09 13:58:30
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：请写一个小游戏，人狗大站;  规则:
    1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
        人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
    2  人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
        人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
    3   对战规则: 
     A  随机决定,谁先开始攻击; 
     B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
     C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
'''
from random import randint
# here put the import lib
class People(object):
    def __init__(self):
        self.life=100
        self.atk=10
    
    def attack(self,enemy):
        enemy.life-=self.atk
        enemy.atk-=3
        if enemy.atk<=0:
            enemy.atk=0
        print("人攻击了狗")
        if enemy.life <= 0:
            print("一只狗死亡")
            return enemy
        return None

class Dog(object):
    def __init__(self):
        self.life=80
        self.atk=15

    def attack(self,enemy):
        enemy.life-=self.atk
        enemy.atk-=2
        if enemy.atk<=0:
            enemy.atk=0
        print("狗攻击了人")
        if enemy.life <= 0:
            print("一个人死亡")
            return enemy

if __name__ == "__main__":
    people=[People(),People()]
    dogs=[Dog(),Dog(),Dog()]
    fighter=randint(0,1)
    while True:
        if fighter == 0:
            i=people[randint(0,len(people)-1)].attack(dogs[randint(0,len(dogs)-1)])
            if i:
                dogs.remove(i)
        elif fighter == 1:
            i=dogs[randint(0,len(dogs)-1)].attack(people[randint(0,len(people)-1)])
            if i:
                dogs.remove(i)
        if len(people)<=0:
            print("狗获胜")
            break
        elif len(dogs)<=0:
            print("人类获胜")
            break
        if fighter == 0:
            fighter=1
        else:
            fighter=0
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
from s5_dog import Dog
from s5_people import People
# here put the import lib

class fight:
    @staticmethod
    def start():#对战类，可输出结果或者直接返回值，1为人类获胜，0为狗获胜
        people=[People(),People()]
        dogs=[Dog(),Dog(),Dog()]
        fighter=randint(0,1)
        for i in range(100000):
            if fighter == 0:
                j=people[randint(0,len(people)-1)].attack(dogs[randint(0,len(dogs)-1)])
                if j:
                    dogs.remove(j)
            elif fighter == 1:
                j=dogs[randint(0,len(dogs)-1)].attack(people[randint(0,len(people)-1)])
                if j:
                    people.remove(j)
            if len(people)<=0:
                # print("狗获胜")
                return 0
            elif len(dogs)<=0:
                # print("人类获胜")
                return 1
            if fighter == 0:
                fighter=1
            else:
                fighter=0
        else:
            print("平局")

if __name__ == "__main__":
    count1=0
    count0=0
    n=10000
    for i in range(n):
        a=fight.start()
        if a==0:
            count0+=1
        elif a==1:
            count1+=1
    print("人类获胜的频率为：{},狗获胜的频率为：{}".format(count1/n,count0/n))
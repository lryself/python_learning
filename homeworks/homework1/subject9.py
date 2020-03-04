# -*- encoding: utf-8 -*-
"""
@File : subject9,
@Time : 2020/3/4 22:27
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；
"""
import random
# here put the import lib
answer=random.randint(0,10)
N=5
for i in range(5):
  a=int(input("请输入你猜测的数字（这是一个在0~10的数），你还有{0}次机会:".format(5-i)))
  if a==answer:
    print("猜对了！")
    break
  else:
    print("猜错了！")
else:
  print("猜测失败！这个数字是：",answer)
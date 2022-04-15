# -*- encoding: utf-8 -*-
'''
@File : s2_judge_weekday.py
@Time : 2020/03/26 18:36:29
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：定义一个函数，判断一个输入的日期，是当年的第几周，周几？
将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）
'''
import datetime
# here put the import lib
weekstr=list("一二三四五六日")
y,m,d=input("请输入年、月、日，用空格隔开：").split()
y=int(y)
m=int(m)
d=int(d)
# y=2020
# m=3
# d=26
date1=datetime.date(y,m,d)
print("这一天是当年的第{}周，是周{}".format(date1.isocalendar()[1],weekstr[datetime.date.isoweekday(date1)-1]))
startnew=datetime.date(2020,2,17)
weeknum=int((date1-startnew).days/7)+1
if weeknum<=27 and weeknum>=1:
    print("这是开学的第{}周".format(weeknum))
else:
    print("不在2020年上半学期的区间")
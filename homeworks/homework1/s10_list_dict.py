# -*- encoding: utf-8 -*-
"""
@File : s10_list_dict
@Time : 2020/3/4 22:38
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
"""

# here put the import lib
# text = input("请输入一段英文文本：\n")
text="One is always on a strange road watching strange scenery and listening to strange music Then one day you will find that the things you tryhard to forget are already gone"
texts1 = list(text.split(" "))

""" 
# 第一种方法
texts2 = {}
for i in texts1:
    if texts2.get(i, 0) == 0:
        texts2[i] = 1
    else:
        texts2[i] = texts2[i] + 1
print(sorted(texts2.items(), key=lambda x: x[1], reverse=True)) """

# 第二种方法
import collections
print(collections.Counter(texts1))
        



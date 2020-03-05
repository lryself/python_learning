# -*- encoding: utf-8 -*-
"""
@File : subject10,
@Time : 2020/3/4 22:38
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
"""

# here put the import lib
# text="One is always on a strange road, watching strange scenery and listeningto strange music. Then one day, you will find that the things you tryhard to forget are already gone."
text=input("请输入一段英文文本：\n")
texts1=list(text.split(" "))
texts2={}
for i in texts1:
  if texts2.get(i, 0) == 0:
    texts2[i]=1;
  else:
    texts2[i]=texts2[i]+1;
print(sorted(texts2.items(),key=lambda x:x[1],reverse=True))

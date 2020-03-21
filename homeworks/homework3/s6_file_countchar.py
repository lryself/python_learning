# -*- encoding: utf-8 -*-
'''
@File : s6_file_countchar.py
@Time : 2020/03/20 22:55:23
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 请读取文章内容,进行词频的统计;
并分别输出统计结果到另外的文件存放;
比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);
'''
import tools
import os
# here put the import lib
def count_char(a):      #统计文章的词频，返还词频最高的10个词
    try:
        with open(a,"r",encoding="utf-8") as f:
            sentence=f.read()
    except OSError:
        print("文件为找到")
    else:
        result = {word: sentence.split().count(word) for word in set(sentence.split())}
        result=sorted(result.items(),key=lambda x: x[1],reverse=True)       #词频排序
        b=[]
        for i in result[:10]:
            b.append(i[0])          #取前十
        return b
art1=count_char("article1.txt")
art2=count_char("article2.txt")
repe=len(art1)+len(art2)-len(set(art1+art2))
print("相似度为：{}0%".format(repe))
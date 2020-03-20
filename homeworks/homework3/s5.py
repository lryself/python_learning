# -*- encoding: utf-8 -*-
'''
@File : s5.py
@Time : 2020/03/20 22:52:17
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
请完成以下文件综合编程迷你项目(提示:可以利用list的insert函数)。
(1)创建一个文件Blowing in the wind.txt,其内容是:
How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind
(2)在文件头部插入歌名"Blowin’ in the wind”
(3)在歌名后插入歌手名"Bob Dylan"
(4)在文件未尾加上字符串"1962 by Warner Bros.Inc"
(5)在屏幕上打印文件内容
'''
import tools
# here put the import lib
strs=[]
try:
    with open("Blowing in the wind.txt","r") as f:
        strs=f.readlines()
except OSError:
    print("打开文件错误！")
else:
    for i in range(len(strs)):
        strs[i]=strs[i].strip("\n")
    strs.insert(0,"Blowin’ in the wind")
    strs.insert(1,"Bob Dylan")
    strs.append("1962 by Warner Bros.Inc")
for i in strs:
    print(i)
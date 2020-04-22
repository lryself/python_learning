# -*- encoding: utf-8 -*-
'''
@File : s1_file_input.py
@Time : 2020/03/20 17:30:52
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
'''
import os
import sys
import tools
# here put the import lib

print(os.getcwd())
print("请输入：")
try:
    with open("input.txt","w") as f:
        while True:
            try:
                f.write(input()+"\n")
            except:
                break
except OSError:
    print("文件打开失败，当前工作目录为：",os.getcwd)
else:
    print("储存完成！")
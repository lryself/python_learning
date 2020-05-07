# -*- encoding: utf-8 -*-
'''
@File : s1_do_os_path.py
@Time : 2020/03/18 08:31:55
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：练习path函数
'''

# here put the import lib
import os
import tools

path1=os.path.abspath("os_practice")
print( os.path.basename(path1) )   # 返回文件名
print( os.path.dirname(path1) )    # 返回目录路径
print( os.path.split(path1) )      # 分割文件名与路径
print( os.path.join('path1','test','run1.txt') )  # 将目录和文件名合成一个路径
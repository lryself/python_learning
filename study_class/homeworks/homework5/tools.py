# -*- encoding: utf-8 -*-
'''
@File : tools.py
@Time : 2020/03/20 19:15:42
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
备注：本程序为存放其他程序的辅助函数
'''
import random
import os
import sys
# here put the import lib

def cur_file_dir(): #用于找到当前文件的目录
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
os.chdir(cur_file_dir())
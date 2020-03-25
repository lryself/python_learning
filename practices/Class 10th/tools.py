# -*- encoding: utf-8 -*-
'''
@File : tools.py
@Time : 2020/03/25 09:58:49
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
辅助程序
'''

# here put the import lib

import os
import sys
# here put the import lib
def cur_file_dir(): #用于找到当前文件的目录
     #获取脚本路径
     path = sys.path[0]
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
os.chdir(cur_file_dir())
# -*- encoding: utf-8 -*-
'''
@File : s4_change_name.py
@Time : 2020/03/20 22:48:05
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png),将当前img目录所有以.png结尾的后缀名改为.jpg.
'''
import tools
import os
# here put the import lib
path=os.path.join(os.getcwd(),"img")
#对目录下的文件进行遍历
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        new_name=file.replace("png","jpg")
        os.rename(os.path.join(path,file),os.path.join(path,new_name))
print ("更改完成")
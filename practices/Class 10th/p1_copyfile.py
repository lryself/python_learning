# -*- encoding: utf-8 -*-
'''
@File : p1_copyfile.py
@Time : 2020/03/25 08:41:22
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：将一个文件夹,拷贝到另外一个文件夹;
'''
import os
import tools
import sys
# here put the import lib
def copyfile(file1,file2):
    file1=os.path.abspath(file1)
    file2=os.path.abspath(file2)
    list1=os.listdir(file1)
    for i in list1:
        j=os.path.join(file2,i)
        if os.path.isfile(os.path.join(file1,i)):
            try:
                f1=open(os.path.join(file1,i),"r",encoding="utf-8")
                f2=open(j,"w")
                list2=f1.readlines()
                f2.writelines(list2)
            except:
                print("打开文件出错")
            finally:
                f1.close()
                f2.close()
        else:
            if not os.path.exists(j):
                os.mkdir(j)
            copyfile(os.path.join(file1,i),j)

if __name__ == "__main__":
    file1="a_file"      #复制源目录
    file2="b_file"      #复制的目标目录
    if not os.path.exists(file2):
        os.mkdir(file2)
    copyfile(file1,file2)
    print("复制完成")
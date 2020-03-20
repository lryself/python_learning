# -*- encoding: utf-8 -*-
'''
@File : s2_file_r&w.py
@Time : 2020/03/20 19:38:05
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
        写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
        #第一行： xxxx
        #第二行： xxxx

'''
import sys
import os
import tools
# here put the import lib

strlines=[]     #文件读取的内容
linenum1=list("零一二三四五六七八九")
linenum2=["","十","百","千","万","十","百","千","亿"]
def getline(i=0):#只能到亿
    if i>1000000000:
        print("数值过大，无法计算")
        return
    j=0;        #位数
    nums=[]
    while(i>0):
        j+=1
        nums.append(int(i%10))
        i=int(i/10)
    linestr=""
    flag=True       #记录是否有连续的零
    nums.reverse()
    for w in range(j):
        if nums[w]==0 and j-w==5:       #万的情况
            if linestr[-1]=="零":
                linestr=linestr[:-1]
                flag=True
            linestr+=linenum2[j-w-1]
        elif nums[w]==1 and j-w==6:     #十万的情况
            linestr+=linenum2[j-w-1]
        elif nums[w]==1 and j-w==2:     #十的情况
            linestr+=linenum2[j-w-1]
        elif nums[w]==0 and flag==True: #连续的零的情况
            linestr+=linenum1[nums[w]]
            flag=False
        elif nums[w]!=0:                #其他情况
            linestr+=linenum1[nums[w]]+linenum2[j-w-1]
            flag=True
    if linestr[-1]=="零":
        linestr=linestr[:-1]
    return linestr

try:
    with open("input.txt","r") as f:
        strlines=f.readlines();
except OSError:
    print("文件打开失败，当前工作目录为：",os.getcwd)
else:
    for i in range(len(strlines)):
        print("第{}行：{}".format(getline(i+1),strlines[i].rstrip("\n")))
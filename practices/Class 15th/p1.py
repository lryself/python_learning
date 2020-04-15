# -*- encoding: utf-8 -*-
'''
@File : p1.py
@Time : 2020/04/15 09:09:22
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：匹配出163的邮箱地址，且@符号之前有4到20位英文或者数字字符，例如hello@163.com
'''
import re
# here put the import lib

ret=re.match("[a-zA-Z0-9]{4,20}@163.com$","hello@163.com")
if ret:
    print(ret.group())
else:
    print("格式错误！")
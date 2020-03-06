# -*- encoding: utf-8 -*-
"""
@File : practice4
@Time : 2020/3/6 9:46
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：使用不定长参数定义一个函数;实现对输入数据的封装(封装成一个列表和字典),然后打印输出;
"""

# here put the import lib
def pack(x,*args):
  data={x:list(args)}
  return data
print(pack(11,22,33,44,55))
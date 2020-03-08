# -*- encoding: utf-8 -*-
"""
@File : s5_function_dict
@Time : 2020/3/8 16:50
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;
"""
# here put the import lib
import re


def check_value(a={}):
  for i in a:
    if type(a[i])==int:
      while a[i] > 100:
        a[i] = int(a[i] / 10)
    elif len(a[i]) > 2:
      a[i] = re.findall(r'.{2}', a[i])[0]
  return a


dict1 = {"a": 123, "b": 4567, "c": "qwert"}
print(check_value(dict1))

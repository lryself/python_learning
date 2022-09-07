# coding: utf-8
# @Author : lryself
# @Date : 2022/6/27 12:10
# @Software: PyCharm

while True:
    s = eval(input())
    if s == 0:
        break
    result = 0
    while s > 1:
        # 先喝汽水
        result += s // 3
        # 剩下的水瓶为s
        # 需要借一个水瓶的情况
        if s % 3 == 2:
            s -= 2
            result += 1
        # 换饮料
        s = s // 3 + s % 3
    print(result)



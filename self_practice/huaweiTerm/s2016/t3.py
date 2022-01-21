# coding: utf-8
# @Author : lryself
# @Date : 2022/1/11 12:43
# @Software: PyCharm

def checkType(s: list) -> int:
    n = len(s)
    # 1个子，2对子，3顺子（连续5张），4三个，5炸弹（四个）6对王
    if n == 1:
        return 1
    if n == 2:
        if s[0] == "joker" or s[0] == "JOKER":
            return 6
        return 2
    if n == 3:
        return 4
    if n == 4:
        return 5
    if n == 5:
        return 3


so = "3 4 5 6 7 8 9 10 J Q K A 2".split()


def checkBigger(a, b):
    c = d = 0
    for index, i in enumerate(so):
        if a == i:
            c = index
        if b == i:
            d = index
    if c > d:
        return True
    return False


s = input()
s1, s2 = s.split("-")
l1 = s1.split()
l2 = s2.split()
r1 = checkType(l1)
r2 = checkType(l2)

if r1 == 6:
    print(s1)
elif r2 == 6:
    print(s2)

elif r1 == 5:
    if r2 != 5:
        print(s1)
    else:
        if checkBigger(l1[0], l2[0]):
            print(s1)
        else:
            print(s2)
elif r2 == 5:
    print(s2)

elif r1 < 5 and r2 < 5:
    if r1 != r2:
        print("ERROR")
    elif checkBigger(l1[0], l2[0]):
        print(s1)
    else:
        print(s2)

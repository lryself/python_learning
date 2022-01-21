# coding: utf-8
# @Author : lryself
# @Software: PyCharm
import datetime
from math import sqrt


def main(num):
    begin = datetime.datetime.now()
    count = 0
    for i in range(10000000):
        if IsPrime(i):
            count += 1
    print("总用时：", datetime.datetime.now()-begin)
    print(num, "以内共有", count, "个质数")


def IsPrime(number):
    if number < 2:
        return False
    if number % 6 != 1 and number % 6 != 5:
        return False
    temp = int(sqrt(number))
    for i in range(5, temp, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


if __name__ == '__main__':
    main(10000000)

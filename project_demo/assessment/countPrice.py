# coding: utf-8
# @Author : lryself
# @Date : 2022/1/24 10:10
# @Software: PyCharm
import random

import numpy as np


def way1(D: list, K: int, n1: int, n2: int) -> float:
    D.sort(reverse=True)
    if n2 == 0:
        RD = D[n1:]
    else:
        RD = D[n1:-n2]
    P = np.mean(RD) * K
    return P


def way2(D: list, n1: int, n2: int, X: int, Y: int) -> float:
    D.sort(reverse=True)
    if n2 == 0:
        RD = D[n1:]
    else:
        RD = D[n1:-n2]
    Ks = (X + Y / 10) / 10
    P = (max(RD) - min(RD)) * Ks + min(RD)
    return P


def way3(D: list, n1: int, n2: int, Q1: float, K1: float, K2: float, BMax: float) -> float:
    D.sort(reverse=True)
    if n2 == 0:
        RD = D[n1:]
    else:
        RD = D[n1:-n2]
    Q2 = 1 - Q1
    P = np.mean(RD) * K1 * Q1 + BMax * K2 * Q2
    return P


# todo D应按照第一轮评审得分排序
def way4(D: list, K: int):
    return np.mean(D[0: 2]) * K


# todo 公式有问题(Nj不在式中)
def way5(D: list, K: int, n1: int, n2: int, N: int):
    if N < 5:
        Nj = N
    else:
        Nj = N - 2
    D.sort(reverse=True)
    if n2 == 0:
        RD = D[n1:]
    else:
        RD = D[n1:-n2]
    return np.mean(RD[0: 2]) * K


def main():
    D = []
    N = 0
    K = random.choice([0.98, 0.985, 0.99, 0.995, 1])
    M = N // 4

    if 0 < N < 6:
        n1 = 0
        n2 = 0
    elif 6 <= N < 10:
        n1 = 1
        n2 = 1
    else:
        n1 = random.randint(1, M - 1)
        n2 = random.randint(1, M + 1)

    way = 0
    if way == 1:
        way1(D, K, n1, n2)
    elif way == 2:
        X = random.randint(2, 6)
        Y = random.randint(2, 6)
        way2(D, n1, n2, X, Y)
    elif way == 3:
        E = 0  # 由招标人自行选取
        Q1 = random.random() * 0.4 + 0.3
        K1 = random.random() * 0.05 + 0.95
        K2 = random.random() * 0.05 + 0.85 + E / 100
        BMax = 0
        way3(D, n1, n2, Q1, K1, K2, BMax)
    elif way == 4:
        way4(D, K)
    elif way == 5:
        way5(D, K, n1, n2, N)


def show_way1(D):
    N = len(D)
    M = N // 4
    result_list = []
    for K in [0.98, 0.985, 0.99, 0.995, 1]:
        result = {}
        result["K"] = K
        if 0 < N < 6:
            n1 = 0
            n2 = 0
            result["n1"] = n1
            result["n2"] = n2
            result["P"] = way1(D, K, n1, n2)
        elif 6 <= N < 10:
            n1 = 1
            n2 = 1
            result["n1"] = n1
            result["n2"] = n2
            result["P"] = way1(D, K, n1, n2)
        else:
            for n1 in range(1, M - 1 + 1):
                for n2 in range(1, M + 1 + 1):
                    result["n1"] = n1
                    result["n2"] = n2
                    result["P"] = way1(D, K, n1, n2)
        result_list.append(result)
    return result_list


def show_way2(D):
    N = len(D)
    M = N // 4
    result_list = []
    for X in range(2, 6+1):
        for Y in range(2, 6+1):
            result = {}
            result["X"] = X
            result["Y"] = Y
            if 0 < N < 6:
                n1 = 0
                n2 = 0
                result["n1"] = n1
                result["n2"] = n2
                result["P"] = way2(D, n1, n2, X, Y)
                result_list.append(result)
            elif 6 <= N < 10:
                n1 = 1
                n2 = 1
                result["n1"] = n1
                result["n2"] = n2
                result["P"] = way2(D, n1, n2, X, Y)
                result_list.append(result)
            else:
                for n1 in range(1, M - 1 + 1):
                    for n2 in range(1, M + 1 + 1):
                        result["n1"] = n1
                        result["n2"] = n2
                        result["P"] = way2(D, n1, n2, X, Y)
                        result_list.append(result)
    return result_list


def show_way3(D, BMax):
    N = len(D)
    M = N // 4
    result_list = []
    for E in range(0, 5+1):
        for Q1 in range(30, 70+1):
            for K1 in range(95, 100+1):
                for K2 in range(85+E, 90+E+1):
                    Q1 = Q1 / 100
                    K1 = K1 / 100
                    K2 = K2 / 100

                    result = {}
                    result["E"] = E
                    result["Q1"] = Q1
                    result["K1"] = K1
                    result["K2"] = K2
                    if 0 < N < 6:
                        n1 = 0
                        n2 = 0
                        result["n1"] = n1
                        result["n2"] = n2
                        result["P"] = way3(D, n1, n2, Q1, K1, K2, BMax)
                        result_list.append(result)
                    elif 6 <= N < 10:
                        n1 = 1
                        n2 = 1
                        result["n1"] = n1
                        result["n2"] = n2
                        result["P"] = way3(D, n1, n2, Q1, K1, K2, BMax)
                        result_list.append(result)
                    else:
                        for n1 in range(1, M - 1 + 1):
                            for n2 in range(1, M + 1 + 1):
                                result["n1"] = n1
                                result["n2"] = n2
                                result["P"] = way3(D, n1, n2, Q1, K1, K2, BMax)
                                result_list.append(result)
    return result_list


if __name__ == '__main__':
    # result = show_way1([random.randint(50, 500) for i in range(10)])
    # result = show_way2([random.randint(50, 500) for i in range(10)])
    result = show_way3([random.randint(50, 500) for i in range(100)], 500)
    print([r["P"] for r in result])

# coding: utf-8
# @Author : lryself
# @Date : 2020/12/24 11:20
# @Software: PyCharm
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        result = []
        temp_len = 0
        temp_index = 0
        for index, i in enumerate(ratings):
            if index == 0:
                result.append(1)
                temp_len += 1
            elif i > ratings[index - 1]:
                result.append(result[-1] + 1)
                if temp_len > 1:
                    for j in range(1, temp_len):
                        result[-index+temp_index-j-1] = max(result[-index+temp_index-j]+1, result[-index+temp_index-j-1])
                temp_len = 1
            elif i < ratings[index - 1]:
                result.append(1)
                temp_index = index
                temp_len += 1
            elif i == ratings[index - 1]:
                result.append(1)
                if temp_len > 1:
                    for j in range(1, temp_len):
                        result[-index+temp_index-j-1] = max(result[-index+temp_index-j]+1, result[-index+temp_index-j-1])
                temp_len = 1

        if temp_len > 1:
            for j in range(1, temp_len):
                result[-j-1] = max(result[-j]+1, result[-j-1])
        return sum(result)

    # def candy(self, ratings: List[int]) -> int:
    #     temp_list = sorted(list(set(ratings)))
    #     temp_dict = {}
    #     for index, i in enumerate(temp_list):
    #         temp_dict[i] = index + 1
    #     result = []
    #     for rate in ratings:
    #         result.append(temp_dict[rate])
    #
    #     if ratings[-1] <= ratings[-2]:
    #         result[-1] = 1
    #     if ratings[0] <= ratings[1]:
    #         result[0] = 1
    #     for i in range(1, len(result) - 1):
    #         if ratings[i] < ratings[i - 1] and ratings[i] < ratings[i + 1]:
    #             result[i] = 1
    #         elif ratings[i] > ratings[i - 1] and ratings[i] > ratings[i + 1]:
    #             result[i] = max(result[i - 1], result[i + 1]) + 1
    #         elif ratings[i - 1] < ratings[i] < ratings[i + 1]:
    #             result = result[i - 1] + 1
    #         elif ratings[i - 1] > ratings[i] > ratings[i + 1]:
    #             result = result[i + 1] + 1
    #     if ratings[-1] == ratings[-2]:
    #         result[-1] = 1
    #     elif ratings[-1] > ratings[-2]:
    #         result[-1] = result[-2] + 1
    #     if ratings[0] == ratings[1]:
    #         result[0] = 1
    #     elif ratings[1] > ratings[0]:
    #         result[1] = result[0] + 1
    #     return sum(result)

# coding: utf-8
# @Author : lryself
# @Date : 2022/7/2 11:31
# @Software: PyCharm


s = input().split()
n = eval(s[0])
r = eval(s[-1])
key_word = s[-2]
words = s[1: n + 1]

key_dict = {}
for i in key_word:
    if i not in key_dict:
        key_dict[i] = 0
    key_dict[i] += 1


def judge_bro(word: str) -> bool:
    if word == key_word:
        return False
    temp_dict = {}
    for i in word:
        if i not in temp_dict:
            temp_dict[i] = 0
        temp_dict[i] += 1
    # for k, v in temp_dict.items():
    #     if k not in key_dict:
    #         return False
    #     if key_dict[k] != v:
    #         return False
    if temp_dict != key_dict:
        return False

    return True


bro_list = []
for i in words:
    if judge_bro(i):
        bro_list.append(i)

bro_list.sort()
print(len(bro_list))
print(bro_list[r-1]) if len(bro_list) > r-1 else None

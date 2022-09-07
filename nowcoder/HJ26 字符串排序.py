# coding: utf-8
# @Author : lryself
# @Date : 2022/7/1 21:58
# @Software: PyCharm

s = input()
n = len(s)
word_pos = {}
pos_sign = []
pos_word = []
for index, i in enumerate(s):
    if "a" <= i <= "z" or "A" <= i <= "Z":
        c = i.lower()
        if c not in word_pos:
            word_pos[c] = []
        word_pos[c].append(index)
keys = list(word_pos.keys())
keys.sort()
for i in keys:
    pos_word.extend(word_pos[i])
index = 0
for i in s:
    if "a" <= i <= "z" or "A" <= i <= "Z":
        print(s[pos_word[index]], end="")
        index += 1
    else:
        print(i, end="")

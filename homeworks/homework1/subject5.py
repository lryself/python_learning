
'''题目：使用random模块，生成随机数，来初始化一个列表，元组；
'''

import random
# here put the import lib
num1 = []
num2 = (random.randint(10, 40))
for i in range(10):
    num1.append(random.randint(0, 20))
print(num1)
print(num2)

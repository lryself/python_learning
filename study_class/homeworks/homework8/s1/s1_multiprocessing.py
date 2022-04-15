# -*- encoding: utf-8 -*-
'''
@File : s1_multiprocessing.py
@Time : 2020/04/24 17:37:37
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：有100个同学的分数：数据请用随机函数生成；
     A 利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
     B 利用线程池来实现；
'''
import tools
import threading
import random
import time
from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED
# here put the import lib
mu=threading.Lock()
def writescore(n):
    print("线程运行")
    data=[]
    for i in range(n):
        data.append(tools.random_name()+" "+str(random.randint(60,100))+"\n")
    mu.acquire()
    with open("students.txt", "a", encoding="utf-8") as f:
        for i in data:
            f.write(i)
    mu.release()
    return None
# 多线程程序
# if __name__ == "__main__":
#     with open("students.txt","w",encoding="utf-8") as f:
#         pass
#     for i in range(5):
#         p=threading.Thread(target=writescore,args=(20,))
#         p.start()
#     while True:
#         if len(threading.enumerate())<=1:
#             break
#         time.sleep(1)
#     print("输出完成")

# 线程池
if __name__ == "__main__":
    with open("students.txt", "w", encoding="utf-8") as f:
        pass
    executor=ThreadPoolExecutor(max_workers=5)
    for i in range(5):
        executor.submit(writescore,20)
    executor.shutdown(True)
    print("输出完成")
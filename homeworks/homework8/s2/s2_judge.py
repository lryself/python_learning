# -*- encoding: utf-8 -*-
'''
@File : s2_judge.py
@Time : 2020/04/25 10:11:38
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
'''
import tools
import re
import requests
from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED
import threading
import queue
import time
# here put the import lib
q=queue.Queue()
mu=threading.Lock()
def judge_url(url):
    # print("进行网址{}的判断".format(url))
    s=""
    try:        # 网络连接有风险，异常处理很重要
        r = requests.get(url,timeout=30)    # 查一下这个方法的使用
        r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
        # f.write(url+" 可以访问\n")
        # q.put(url+" 可以访问\n")
        s=url+" 可以访问\n"
    except:
        # f.write(url+" 不能访问\n")
        # q.put(url+" 不能访问\n")
        s=url+" 不能访问\n"
    mu.acquire()
    with open("url_data_answer.txt","a",encoding="utf-8") as f:
        f.write(s)
    mu.release()

if __name__ == "__main__":
    t1=time.time()
    f=open("url_data.txt","r")
    po=ThreadPoolExecutor(max_workers=50)
    # alltask=[]
    with open("url_data_answer.txt","w",encoding="utf-8") as f1:
        pass
    # f1=open("url_data1.txt","w",encoding="utf-8")
    for i in f:
        q=re.split(";|,",i)
        for j in q:
            j=j.strip()
            res=re.search(r"(http[s]?://)?([a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|[\u4e00-\u9fa5])+",j)
            url=""
            if re.match("^http://.*",res.group()):
                url=res.group()
            else:
                url="http://"+res.group()
            po.submit(judge_url,url)
            # judge_url(f1,url)
            # po.submit(f1.write(url+"\n"))
    po.shutdown(True)
    # f1.close()
    f.close()
    print("输出完成")
    t2=time.time()
    print(t2-t1)
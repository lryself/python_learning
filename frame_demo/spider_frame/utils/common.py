# coding: utf-8
# @Author : lryself
# @Date : 2022/7/28 0:31
# @Software: PyCharm

import asyncio
import random
from multiprocessing import cpu_count, Pool


def get_random_user_agent() -> str:
    with open("./resource/user_gent.txt", "r") as f:
        lines = f.readlines()
    return random.choice(lines)


def init_asyncio_pool(tasks):
    loop = asyncio.get_event_loop()
    # tasks = []
    # for url in urls:
    #     task = download_pdf(url[0], url[1])
    #     task_loop = loop.create_task(task)  # 定义事件循环
    #     tasks.append(task_loop)
    loop.run_until_complete(asyncio.wait(tasks))


def init_pool(func, *args):
    pool = Pool(cpu_count() * 2 + 1)
    for arg in args:
        pool.apply_async(func, arg)
    pool.close()
    pool.join()


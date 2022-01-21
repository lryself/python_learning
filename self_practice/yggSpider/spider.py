# coding: utf-8
# @Author : lryself
# @Date : 2021/6/11 15:40
# @Software: PyCharm
import asyncio
import csv
from multiprocessing import Pool, cpu_count

import aiohttp
import requests


def get_all_urls():
    with open("urls.csv", "r", encoding="utf-8") as f:
        csvFile = csv.reader(f)
        header = next(csvFile)
        urls = []
        for row in csvFile:
            urls.append(row)
        return urls


async def download_pdf(pdf_name, pdf_url):
    print(f"开始下载 {pdf_name}")
    try:
        async with aiohttp.ClientSession() as session:
            async with await session.get(url=pdf_url, timeout=10) as response:
                pdf_bin = await response.read()
    except Exception as e:
        print(e)

    async with open(f"files/{pdf_name}", "wb") as f:
        await f.write(pdf_bin)
    print(f"下载完成 {pdf_name}")


if __name__ == '__main__':
    urls = get_all_urls()
    loop = asyncio.get_event_loop()
    tasks = []
    for url in urls:
        task = download_pdf(url[0], url[1])
        task_loop = loop.create_task(task)  # 定义事件循环
        tasks.append(task_loop)
    loop.run_until_complete(asyncio.wait(tasks))

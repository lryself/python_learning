# coding: utf-8
# @Author : lryself
# @Date : 2021/2/27 11:30
# @Software: PyCharm
import asyncio
from datetime import datetime
from multiprocessing import Pool, cpu_count
import aiohttp
from bs4 import BeautifulSoup
import requests


# 转化图片url
def re_picture_url(old_url):
    picture_name = old_url.split('/')[-1]
    new_url = old_url.replace("https://th.wallhaven.cc/small", "https://w.wallhaven.cc/full", 1)
    new_url = new_url.replace(picture_name, "wallhaven-" + picture_name, 1)
    return new_url


# 解析页面上所有图片url
def parse_page(page_url):
    response = requests.get(page_url)
    bs = BeautifulSoup(response.text, "lxml")
    image_tags = bs.find("section", class_="thumb-listing-page").find_all("img")
    image_urls = []
    for tag in image_tags:
        image_urls.append(re_picture_url(tag.attrs["data-src"]))
    return image_urls


def download_picture_page(page_url):
    picture_urls = parse_page(page_url)
    loop = asyncio.get_event_loop()
    tasks = []
    for picture_url in picture_urls:
        task = download_picture(picture_url)  # 创建一个下载任务--异步IO对象
        task_loop = loop.create_task(task)       # 定义事件循环
        tasks.append(task_loop)
    loop.run_until_complete(asyncio.wait(tasks))


# 程序入口
def main():
    pool = Pool(cpu_count() * 2 + 1)
    for page in range(1, 5):
        pool.apply_async(download_picture_page, (f"https://wallhaven.cc/search?categories=100&purity=100&ratios=16x9&topRange=1M&sorting=toplist&order=desc&page={page}",))
    pool.close()
    pool.join()

    print("下载完成！")


async def download_picture(picture_url):
    picture_name = picture_url.split('/')[-1]
    print(f"开始下载{picture_name}")
    try:
        async with aiohttp.ClientSession() as session:
            async with await session.get(url=picture_url, timeout=10) as response:
                picture_bin = await response.read()
    except Exception as e:
        print(e)
    # print(f"下载完成{picture_name}")
    print(f"开始写入{picture_name}")
    with open(f"download/{picture_name}", 'wb') as f:
        f.write(picture_bin)
    print(f"写入完成{picture_name}")


def download_file(file_url):
    file_name = file_url.split('/')[-1]
    print(f"开始下载{file_name}")
    file_bin = requests.get(file_url).content
    # print(f"下载完成{picture_name}")
    print(f"下载完成{file_name}开始写入")
    with open(f"download/{file_name}", 'wb') as f:
        f.write(file_bin)
    print(f"写入完成{file_name}")


if __name__ == '__main__':
    start = datetime.now()
    download_file("https://images.pexels.com/photos/4577736/pexels-photo-4577736.jpeg")
    print(start-datetime.now())

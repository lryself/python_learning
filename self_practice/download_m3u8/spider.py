# coding: utf-8
# @Author : lryself
# @Date : 2021/11/24 3:31
# @Software: PyCharm
import os
import re

import requests


def spdier_m3u8(m3u8_url):
    m3u8_name = re.search(r"mp4.+m3u8", m3u8_url).group().lstrip("mp4").strip("/")
    res = requests.get(m3u8_url)
    ts_text = res.text

    with open(f"{video_hash}.m3u8", "w", encoding="utf-8") as f:
        f.write(ts_text)
    ts_list = []
    for l in re.findall(r"mp4.+ts", ts_text):
        ts_url = m3u8_url.replace(m3u8_name, l.lstrip("mp4"))
        ts_list.append(ts_url + "\n")
    with open("ts_list.txt", "w", encoding="utf-8") as f:
        f.writelines(ts_list)

    return video_hash


def spider_ts():
    with open("ts_list.txt", "r", encoding="utf-8") as f:
        ts_list = f.readlines()

    for index, ts_url in enumerate(ts_list):
        file_name = re.search(r"mp4.+ts", ts_url).group().lstrip("mp4").lstrip("/")
        try:
            res = requests.get(ts_url.rstrip("\n"))
        except Exception as e:
            print(f"Error {e}")
            return
        with open(file_name, "wb") as f:
            f.write(res.content)
            print(f"完成{index + 1}/{len(ts_list)}({(index + 1) / len(ts_list) * 100}%)")


def combat(video_name):
    with open("ts_list.txt", "r", encoding="utf-8") as f:
        ts_list = f.readlines()
    with open(f"../{video_name}.mp4", "wb") as f:
        for index, ts_url in enumerate(ts_list):
            file_name = re.search(r"mp4.+ts", ts_url).group().lstrip("mp4").lstrip("/")
            with open(file_name, "rb") as f1:
                f.write(f1.read())


if __name__ == '__main__':
    url = "XXX"

    video_hash = re.search("hash=[0-9a-z]+", url).group()[5:]
    video_path = "video/" + video_hash
    if not os.path.exists(video_path):
        os.makedirs(video_path)
    os.chdir(video_path)

    # spdier_m3u8(url)
    # spider_ts()
    combat(video_hash)

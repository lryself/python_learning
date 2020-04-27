# -*- encoding: utf-8 -*-
'''
@File : s3_download.py
@Time : 2020/04/19 20:24:37
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/；  请大家写一个爬虫，将里面的英语节目MP3，都下载下来；
     这些音频文件 在网页的html文件内容都是以mp3结尾的，如下图所示：

   要求大家使用Requests库获取这个网页html文本内容，并且使用正则表达式获取里面所有的mp3文件的网址；并进行下载；
  Windows上的wget可以点击这里 下载。 这个程序不用安装，直接在命令行里使用即可；
注意：
获取的音频网址前面需要加上 前缀 http://www.listeningexpress.com/studioclassroom/ad/ 才是完整的下载地址
MP3文件中有空格字符，组成下载网址时，需要进行url编码，否则空格会被当成命令行分隔符。参考代码如下所示
>>> from urllib.parse import quote
>>> quote('2019-04-13 NEWSworthy Clips.mp3')
'2019-04-13%20NEWSworthy%20Clips.mp3'
'''
from urllib import request
import requests
import re
from urllib.parse import quote
import tools
import wget
import os
from multiprocessing import Pool
# here put the import lib


@tools.count_time
def down_MP3(urls, file_name):
    os.chdir(down_path)

    # 迭代1：增加进程池
    # po=Pool(8)

    for j in set(urls):
        file_url = base_url + quote(j)
        try:
            # 未知原因wget无法使用
            # wget.download(j)
            request.urlretrieve(file_url, os.path.join(file_name, j))
            print("下载成功")

            # 迭代1：增加多进程的使用
            # po.apply_async(func=request.urlretrieve,args=(file_url, os.path.join(file_name, j),))

        except BaseException as e:
            # print(e)
            print("下载失败")
    # 迭代1：进程池的结束
    # po.close()
    # po.join()

    print("全部下载完成")
    # 测试wget没有问题，可以下载MP3
    # try:
    #     wget.download("http://fs.w.kugou.com/201903281113/775fe3d7139e7c859a427268f56e3470/G083/M09/03/0F/kw0DAFggQruAHHzNADLKHpoVYyI896.mp3",out="测试.mp3")
    # except BaseException as e:
    #     print(e)
    #     print("下载失败")


base_url = "http://www.listeningexpress.com/studioclassroom/ad/"

# 音频下载地址
if not os.path.exists("download"):
    os.mkdir("download")
down_path = os.path.join(os.path.abspath(os.getcwd()), "download")

try:
    r = requests.get(base_url)
except BaseException as e:
    print(e)
    print("打开网址出错！")
else:
    res = re.findall(r"sc-ad[a-zA-Z0-9 -.]+.mp3", r.text)

    # 下载
    down_MP3(res, down_path)

    # 写网址到文件
    # with open("s3_urltext.txt", "w", encoding="utf-8") as f:
    #     for i in set(res):
    #         f.write(base_url + quote(i) + "\n")

# -*- encoding: utf-8 -*-
'''
启动爬虫项目
'''
from scrapy import cmdline
# here put the import lib
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
cmdline.execute(["scrapy", "crawl", "51job"])
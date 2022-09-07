# coding: utf-8
# @Author : lryself
# @Date : 2022/7/28 1:25
# @Software: PyCharm
import requests
from requests import Session
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup


def get_requests_session(max_retries: int = 5) -> Session:
    requests_session = requests.session()
    requests_session.mount('http://', HTTPAdapter(max_retries=max_retries))
    requests_session.mount('https://', HTTPAdapter(max_retries=max_retries))
    requests_session.keep_alive = False
    return requests_session


def parse_html(html: str, parse: str = "lxml"):
    # html.parser, lxml, html5lib, lxml-xml
    return BeautifulSoup(html, parse)

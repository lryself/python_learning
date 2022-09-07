# coding: utf-8
# @Author : lryself
# @Date : 2022/7/31 10:52
# @Software: PyCharm

def get_statuscode() -> dict:
    status_codes = {}
    with open("../resource/status_codes.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            code = line.split()
            status_codes[code[0]] = {
                "message": code[1],
                "describe": code[2]
            }

    return status_codes


def get_useragent() -> list:
    with open("../resource/user_agent.txt", "r", encoding="utf8") as f:
        user_agents = f.readlines()
    return user_agents


def get_cookie() -> list:
    with open("../resource/cookie.txt", "r", encoding="utf8") as f:
        cookies = f.readlines()
    return cookies

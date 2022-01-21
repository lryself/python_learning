# coding: utf-8
# @Author : lryself
# @Date : 2021/12/28 22:55
# @Software: PyCharm

from .controller import *

session = {}


session["allow_query_paper"] = []


class PaperApi:
    @classmethod
    def get_papersInfo_by_userID(cls):
        parser = {}
        result = UserController.get_user(parser["UserID"])

        deal("获取系统秘钥并通过秘钥做rsa解密")
        deal("验证密码")

        token = deal("签发token")

        result = TokenController.add_token(token)

        deal(result, "如果加入数据库失败返回值")

        return result

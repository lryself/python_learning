# coding: utf-8
# @Author : lryself
# @Date : 2021/12/28 22:55
# @Software: PyCharm
from .commons import *
from .service import *


class UserController:
    @classmethod
    def get_user(cls, userid):
        deal(userid)

        result = UserManager.get(userid)

        deal(result)

        return result


class TokenController:
    @classmethod
    def add_token(cls, token):
        deal(token)
        deal("验证token格式是否为string而不是byte")

        result = TokenManager.add(token)

        deal(result, "是否添加成功")

        return result

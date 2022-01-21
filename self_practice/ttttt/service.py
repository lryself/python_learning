# coding: utf-8
# @Author : lryself
# @Date : 2021/12/28 22:55
# @Software: PyCharm


from .model import *


class UserManager(UserModel):
    @classmethod
    def get(cls, userid):
        result = UserModel()
        return result


class TokenManager(TokenModel):
    @classmethod
    def add(cls, token):
        result = TokenModel()
        return result
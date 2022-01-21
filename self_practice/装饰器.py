# coding: utf-8
# @Author : liruiyang
# @File : ClassResource
# @Software: PyCharm

from functools import wraps


# 用户身份验证（解决垂直越权问题）
def verify_usertype(allow_users: list, *args, **kwargs):
    """
    获取装饰器的传参
    """
    def _verify_usertype(func):
        """
        获取函数
        """
        @wraps(func)
        def wrapper(*func_args, **func_kwargs):
            """
            获取函数传参
            """
            if 1 not in allow_users:
                print("未通过验证！")
                return
            print('现在开始装饰')
            func(*func_args, **func_kwargs)
            print('现在结束装饰')
        return wrapper
    return _verify_usertype


@verify_usertype([1, 2, 3, 4, 5, 6])
def test():
    print("hallo world")


if __name__ == '__main__':
    test()
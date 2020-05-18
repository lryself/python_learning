# -*- encoding: utf-8 -*-
"""
@File : testModels
@Time : 2020/5/18 18:15
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from app.models import StuChoose
from app import db
# here put the import lib
# class UserTest(unittest.TestCase):
#     def testfind_stu(self):
#         word='stu1'
#         value='123456'
#         self.assertEqual(value,models.User.find_stu('name', word))


def find_id(word='user', value='', *args):
    res = db.session.query(StuChoose).filter(StuChoose.user == value).all()
    return res

if __name__ == '__main__':
    print(find_id(value='stu1'))

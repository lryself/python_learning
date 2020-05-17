# -*- encoding: utf-8 -*-
"""
@File : testUserself
@Time : 2020/5/16 21:20
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
import unittest
from User import Userself
# here put the import lib

class UserselfTest(unittest.TestCase):
    def testload(self):
        u1='stu1'
        u2='123456'
        user1=Userself(u1,u2,1)
        self.assertEqual(user1.load(),True)

    def testadd_class(self):
        temp = Userself('stu1', '123456', 1)
        self.assertEqual(temp.add_class(1),True)

    def testdel_class(self):
        temp = Userself('stu1', '123456', 1)
        self.assertEqual(temp.del_class(1),True)

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTests([UserselfTest('testload'),UserselfTest('testadd_class'),UserselfTest('testdel_class')])
    unittest.TextTestRunner().run(suite)



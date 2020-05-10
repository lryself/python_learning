# -*- encoding: utf-8 -*-
"""
@File : s2
@Time : 2020/5/8 15:45
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
   使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；
"""
import pymysql
import os
# here put the import lib


def sql_send(sql):
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        print("SQL语句执行成功")
        return cursor
    except Exception as e:
        print(e)
        print("SQL语句执行失败！")
        db.rollback()


def choose():
    '''
    页面初始化

    :Return:返回用户选择的操作
    '''
    os.system('cls')
    print("您可以进行如下数据库操作：")
    i = 0
    print("{}.退出".format(i))
    i += 1
    print("{}.增加留言信息".format(i))
    i += 1
    print("{}.删除留言信息".format(i))
    i += 1
    print("{}.修改留言信息".format(i))
    i += 1
    print("{}.查询留言信息".format(i))
    i += 1
    print("{}.输出全部留言".format(i))
    i += 1
    try:
        n = int(input("请输入您要进行的操作数："))
        if n < 0 or n >= i:
            raise Exception
        return n
    except Exception:
        print("您输入的操作数有误，请重新输入！")


if __name__ == '__main__':
    try:
        # 连接数据库
        db = pymysql.connect(
            "rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com",
            "rj1801lry",
            "lry12345678",
            "python_learn")
    except Exception as e:
        print(e)
        print("数据库连接失败！")
    else:
        while True:
            n = choose()
            if n == 0:
                break
            elif n == 1:
                contents = input("请输入留言：")
                people = input("请输入留言人：")
                sql = """INSERT INTO guestbook(contents,people)VALUES (\"{}\", \"{}\")""".format(contents, people)
                sql_send(sql=sql)
            elif n == 2:
                m_id = input("请输入您要删除的留言id：")
                sql = """UPDATE guestbook SET is_delete = 1 WHERE id = \"{}\"""".format(m_id)
                sql_send(sql)
            elif n == 3:
                m_id = input("请输入您要修改的留言id：")
                m_word = input("请输入您要修改的字段：")
                m_value = input("请输入您要修改的值：")
                sql = """UPDATE guestbook SET {} = \"{}\" WHERE id={}""".format(m_word, m_value, m_id)
                sql_send(sql)
            elif n == 4:
                m_word = input("请输入您要查询的字段：")
                m_value = input("请输入您要查询的值：")
                sql = """SELECT * FROM guestbook WHERE {} = \"{}\" AND is_delete = 0""".format(m_word, m_value)
                res = sql_send(sql)
                if res is not None:
                    if res.rowcount == 0:
                        print("查询结果为空！")
                    else:
                        print("{:<5}{:50}{:>10}{:>30}".format("id", "contents", "people", "time"))
                        for i in res:
                            print("{:<5}{:50}{:>10}{:>30}".format(i[0], i[1], i[2], i[3].strftime('%b-%d-%Y %H:%M:%S')))
            elif n == 5:
                sql = """SELECT * FROM guestbook"""
                res = sql_send(sql)
                if res is not None:
                    if res.rowcount == 0:
                        print("查询结果为空！")
                    else:
                        print("{:<5}{:50}{:>10}{:>30}{:>10}".format("id", "contents", "people", "time", "is_delete"))
                        for i in res:
                            print("{:<5}{:50}{:>10}{:>30}{:>10}".format(
                                i[0], i[1], i[2], i[3].strftime('%b-%d-%Y %H:%M:%S'), i[4]))

            input("按回车继续")
        db.close()

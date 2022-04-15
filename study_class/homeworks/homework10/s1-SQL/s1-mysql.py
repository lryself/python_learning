# -*- encoding: utf-8 -*-
"""
@File : s1-mysql
@Time : 2020/5/8 15:33
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
针对我们给大家的2张表（学生表和班级表），做以下查询；（查询脚本放在一个文件中，创建一个SQL文件夹，放到这个里面，最后提交到代码仓库）
① 查询所有男生的姓名，年龄，所在班级名称；
② 查询所有查询编号小于4或没被删除的学生；
③ 查询姓黄并且“名”是一个字的学生；
④ 查询编号是1或3或8的学生
⑤ 查询编号为3至8的学生
⑥ 查询未删除男生信息，按年龄降序
⑦ 查询女生的总数
⑧ 查询学生的平均年龄
⑨ 分别统计性别为男/女的人年龄平均值
⑩ 按照性别来进行人员分组如下显示（group by + group_concat()）；
    | 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                                 |
	| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                        |
	| 中性   | 金星                                                       |
	| 保密   | 凤姐                                                       |
"""
import os
import pymysql


# here put the import lib


def base(func):
    def base1(*args):
        try:
            args[1].execute(args[2])
            if len(args) == 4:
                func(self=args[0], res=args[1].fetchall(), strs=args[3])
            else:
                func(self=args[0], res=args[1].fetchall())
        except Exception as e:
            print(e)
            print("查询失败！")

    return base1


class Solution:

    def __init__(self, cursor):
        self.cursor = cursor

    # def commod1(self):
    #     '''
    #     查询所有男生的姓名，年龄，所在班级名称
    #     '''
    #     sql = """SELECT name,age,cls_id FROM students WHERE gender="男" """
    #     try:
    #         self.cursor.execute(sql)
    #         res = self.cursor.fetchall()
    #         print("{:<8}{:<4}{:<4}".format("姓名","年龄","班级"))
    #         for row in res:
    #             name=row[0]
    #             age=row[1]
    #             cls_id=row[2]
    #             print("{n:<10}{a:<6}{c:<4}".format(n=name,a=age,c=cls_id))
    #     except Exception as e:
    #         print(e)
    #         print("查询失败！")

    @base
    def commod1(self, res):
        """
        查询所有男生的姓名，年龄，所在班级名称
        """
        print("{:<8}{:<4}{:<4}".format("姓名", "年龄", "班级"))
        for row in res:
            name = row[0]
            age = row[1]
            cls_id = row[2]
            print("{n:<10}{a:<6}{c:<4}".format(n=name, a=age, c=cls_id))

    @base
    def commod2(self, res):
        """
        标准输出
        """
        print(
            "{:<5}{:<10}{:<8}{:<10}{:<5}{:<5}".format(
                "序号",
                "姓名",
                "年龄",
                "身高",
                "性别",
                "班级"))
        for i in res:
            self.print_stu(i)

    @base
    def commod3(self, res, strs=""):
        """
        输出统计结果
        """
        print("{}：{}".format(strs, res[0][0]))

    @base
    def commod4(self, res, strs=""):
        """
        分组显示
        """
        ans = ""
        for i in res:
            ans += "{},".format(i[0])
        print("|{:<10}|{:100}|".format(strs, ans.rstrip(",")))

    @classmethod
    def print_stu(cls, row):
        ans = []
        for i in range(len(row)):
            if row[i] is None:
                ans.append('null')
            else:
                ans.append(row[i])
        print("{:<7}{:<10}{:<8}{:<10}{:>5}{:>5}".format(
            ans[0], ans[1], ans[2], ans[3], ans[4], ans[5]))


def choose():
    '''
    页面初始化

    :Return:返回用户选择的操作
    '''
    os.system('cls')
    print("您可以进行如下数据库操作：")
    print("0.退出")
    print("1.查询所有男生的姓名，年龄，所在班级名称")
    print("2.查询所有查询编号小于4或没被删除的学生")
    print("3.查询姓黄并且“名”是一个字的学生")
    print("4.查询编号是1或3或8的学生")
    print("5.查询编号为3至8的学生")
    print("6.查询未删除男生信息，按年龄降序")
    print("7.查询女生的总数")
    print("8.查询学生的平均年龄")
    print("9.分别统计性别为男/女的人年龄平均值")
    print("10.按照性别来进行人员分组如下显示（group by + group_concat()）")
    try:
        n = int(input("请输入您要进行的操作数："))
        if n < 0 or n > 10:
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
        print("数据库连接失败")
    else:
        so = Solution(db.cursor())
        while True:
            n = choose()
            print("您要进行的是操作{}！".format(n))
            if n == 0:
                break
            elif n == 1:
                sql = """SELECT name,age,cls_id FROM students WHERE gender="男" """
                so.commod1(so.cursor, sql)
            elif n == 2:
                sql = """SELECT * FROM students WHERE id<4 AND is_delete=0"""
                so.commod2(so.cursor, sql)
            elif n == 3:
                sql = """SELECT * FROM students WHERE name LIKE '黄_'"""
                so.commod2(so.cursor, sql)
            elif n == 4:
                sql = """SELECT * FROM students WHERE id=1 OR id=3 OR id=8"""
                so.commod2(so.cursor, sql)
            elif n == 5:
                sql = """SELECT * FROM students WHERE id>=3 AND id <=8"""
                so.commod2(so.cursor, sql)
            elif n == 6:
                sql = """SELECT * FROM students WHERE is_delete=0 AND gender="男" ORDER BY age DESC"""
                so.commod2(so.cursor, sql)
            elif n == 7:
                sql = """SELECT COUNT(*) AS nums FROM students WHERE gender="女" """
                so.commod3(so.cursor, sql, "女生的总数")
            elif n == 8:
                sql = """SELECT AVG(age) AS ages FROM students"""
                so.commod3(so.cursor, sql, "学生的平均年龄")
            elif n == 9:
                sql1 = """SELECT AVG(age) FROM students WHERE gender="男" """
                sql2 = """SELECT AVG(age) FROM students WHERE gender="女" """
                so.commod3(so.cursor, sql1, "男生的平均年龄")
                so.commod3(so.cursor, sql2, "女生的平均年龄")
            elif n == 10:
                sql1 = """SELECT name FROM students WHERE gender="男" """
                sql2 = """SELECT name FROM students WHERE gender="女" """
                sql3 = """SELECT name FROM students WHERE gender="中性" """
                sql4 = """SELECT name FROM students WHERE gender="保密" """
                so.commod4(so.cursor, sql1, "男生")
                so.commod4(so.cursor, sql2, "女生")
                so.commod4(so.cursor, sql3, "中性")
                so.commod4(so.cursor, sql4, "保密")

            input("按回车继续")
        db.close()

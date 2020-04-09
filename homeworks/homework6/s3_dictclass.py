# -*- encoding: utf-8 -*-
'''
@File : s3.py
@Time : 2020/04/09 10:07:43
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：定义一个字典类：dictclass。完成下面的功能：
    dict = dictclass({你需要操作的字典对象})
    1 删除某个key
    del_dict(key)
    2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
    get_dict(key)
    3 返回键组成的列表：返回类型;(list)
    get_key()
    4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
    update_dict({要合并的字典})

'''

# here put the import lib
class dictclass(object):
    def __init__(self,value={}):
        self.value=value

    def del_dict(self,key):
        del self.value[key]
    
    def get_dict(self,key):
        if key in self.value:
            return self.value[key]
        elif key not in self.value:
            return "not found"
    
    def get_key(self):
        return list(self.value.keys())
    
    def update_dict(self,newdict):
        self.value.update(newdict)
        return list(self.value.values())

if __name__ == "__main__":
    data1={"张三":18,"李四":18,"王五":18}
    dict=dictclass(data1)
    dict.del_dict("张三")
    print(dict.value)
    print(dict.get_dict("李四"))
    print(dict.get_dict("刘六"))
    print(dict.get_key())
    print(dict.update_dict({"刘六":30}))

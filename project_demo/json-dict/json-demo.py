# 转换到当前目录
import os
import sys


def cur_file_dir():
    '''
    用于找到当前文件的目录

    :return:返回一个绝对路径
    '''
    # 获取脚本路径
    path = sys.path[0]
    # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


os.chdir(cur_file_dir())

# 以下是正文
import json


def json_operation(json_data, operate, **kwargs):
    if operate == 'add':
        dict_data = []
        for i in kwargs.items():
            new_dict = {i[0]: i[1], 'Status': 0}
            dict_data.append(new_dict)
        json_data.extend(dict_data)
    if operate == 'delete':
        dict_data = list(kwargs.items())
        for j in dict_data:
            for i in json_data:
                res = i.get(j[0], None)
                if res:
                    if res == j[1]:
                        json_data.remove(i)
    return json_data


if __name__ == "__main__":
    data = {'secretaID': '23456', 'TeacherID': '12345'}
    operation = 'add'
    with open('test-demo.json', 'w', encoding='utf-8') as fp:
        fp.write('''[
{
    "StudentID":20200422269,
    "Status":1
},
{
    "TutorID":42,
    "Status":0
},
{
    "CrossTutorID":"41",
    "Status":0
},
{
    "CrossTutorID":"20200610001",
    "Status":0
}
]''')
    with open('test-demo.json', 'r', encoding='utf-8') as fp:
        json_data = json.load(fp)
    with open('test-demo.json', 'w', encoding='utf-8') as fp:
        json.dump(json_operation(json_data=json_data, operate=operation, **data), fp, ensure_ascii=False)

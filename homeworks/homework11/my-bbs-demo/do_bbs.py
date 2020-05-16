#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bbs.bbsModel import BBsModel

if __name__ == '__main__':
    # 添加留言
    kwargs={
          'username':'jackie',
          'content':'天天向上！'
    }

    result_dict = BBsModel.add_bbs(**kwargs)

    if result_dict.get('code') == '200':
        print("记录插入成功！")
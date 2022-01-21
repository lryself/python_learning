# coding: utf-8
# @Author : lryself
# @Date : 2021/1/12 18:20
# @Software: PyCharm
import os
import flask_sqlalchemy
import sqlalchemy


def read_all_object(cmd):
    if not os.path.exists("models"):
        os.mkdir("models")
    os.system(cmd)

    make_model_code()

    with open("models/models.py", "a", encoding="utf-8") as f:
        f.write("\nclass_dict = {key: var for key, var in locals().items() if isinstance(var, type)}\n")

    from models.models import class_dict

    object_list = []
    for c in class_dict.items():
        if type(c[1]) is flask_sqlalchemy.model.DefaultMeta:
            object_list.append(c[1])

    return object_list


def make_manager_service_code(_model):
    manager_templetes = \
        '''from ..models.{{model_file_name}}Model import {{class_name}} as _{{class_name}}

from flask import current_app
from ..models import db
from ..utils.commons import fPrint_id_by_time, query_to_dict
from ..utils.response_code import *


class {{class_name}}Manager(_{{class_name}}):
    @classmethod
    def add(cls, **kwargs):
{{all_args}}
        filter_list = []
{{all_filter}}
        # 检查是否有重复的邮箱
        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if result_model.first():
            return code_has_data()

        new_id = fPrint_id_by_time()
        # 生成用户id 插入信息到表里
        try:
            NewModel = cls.__call__(
{{all_attrs}}
            )
            db.session.add(NewModel)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return code_db_error(e)

        return code_ok()

    @classmethod
    def delete(cls, **kwargs):
{{all_args}}
        filter_list = []
{{all_filter}}
        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        try:
            result_model.delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return code_db_error(e)

        result = query_to_dict(result_model.first())
        return code_ok(data=result)

    @classmethod
    def update(cls, **kwargs):
{{all_args}}

        filter_list = []
{{all_filter}}
        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        args = {}
{{all_update_attrs}}
        try:
            result_model.update(args)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return code_db_error(e)

        result = query_to_dict(result_model.first())
        return code_ok(data=result)

    @classmethod
    def get(cls, **kwargs):
{{all_args}}
        filter_list = []
{{all_filter}}
        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        result = query_to_dict(result_model.first())
        return code_ok(data=result)

    @classmethod
    def get_list(cls, **kwargs):
{{all_args}}
        filter_list = []
{{all_filter}}
        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        result = query_to_dict(result_model.all())
        return code_ok(data=result)
'''

    service_templete = \
        '''from ..manager.{{model_file_name}}Manager import {{class_name}}Manager as _{{class_name}}Manager


class {{class_name}}Service(_{{class_name}}Manager):
    pass
'''

    model_file_name = _model.__name__[0].lower() + _model.__name__[1:]

    class_name = _model.__name__

    all_args = ""
    all_filter = ""
    all_attrs = ""
    all_update_attrs = ""
    for arg in _model.__dict__.keys():
        if "_" not in arg and type(_model.__dict__.get(arg)) == sqlalchemy.orm.attributes.InstrumentedAttribute:
            all_args += f"        {arg} = kwargs.get('{arg}')\n"
            all_filter += f"        if {arg}:\n            filter_list.append(cls.{arg} == {arg})\n"
            all_attrs += f"                {arg}={arg},\n"
            all_update_attrs += f"        if {arg}:\n            args['{arg}'] = {arg}\n"

    manager_templetes = manager_templetes.replace("{{model_file_name}}", model_file_name)
    manager_templetes = manager_templetes.replace("{{class_name}}", class_name)
    manager_templetes = manager_templetes.replace("{{all_args}}", all_args)
    manager_templetes = manager_templetes.replace("{{all_attrs}}", all_attrs)
    manager_templetes = manager_templetes.replace("{{all_filter}}", all_filter)
    manager_templetes = manager_templetes.replace("{{all_update_attrs}}", all_update_attrs)

    if not os.path.exists("manager"):
        os.mkdir("manager")
    with open("manager/{}.py".format(model_file_name + "Manager"), "w", encoding="utf-8") as f:
        f.write(manager_templetes)

    service_templete = service_templete.replace("{{model_file_name}}", model_file_name)
    service_templete = service_templete.replace("{{class_name}}", class_name)
    if not os.path.exists("service"):
        os.mkdir("service")
    with open("service/{}.py".format(model_file_name + "Service"), "w", encoding="utf-8") as f:
        f.write(service_templete)


def make_model_code():
    model_templetes = '''# coding: utf-8
from . import db


'''
    import re

    with open("models/models.py", "r", encoding="utf-8") as f:
        str_lines = f.readlines()
        m = ""
        name = ""
        for line in str_lines:
            if re.match("^(class|t_).*:", line):
                if not m == "":
                    with open(name, "w", encoding="utf-8") as f1:
                        f1.write(m)
                name = "models/{}Model.py".format(line[6].lower() + line[7:-12])
                m = model_templetes + line
            elif re.match("^(from|db|#|\n).*", line):
                continue
            else:
                m += line
        else:
            with open(name, "w", encoding="utf-8") as f1:
                f1.write(m)


if __name__ == '__main__':
    cmd = 'flask-sqlacodegen mysql+pymysql://lryself:lpc123LPC@rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com:3306/school_dachaung?charset=utf8 --outfile "models/models.py"  --flask'
    for c in read_all_object(cmd=cmd):
        make_manager_service_code(c)
    print("创建文件完成！")

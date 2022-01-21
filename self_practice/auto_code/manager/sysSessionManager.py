from ..models.sysSessionModel import SysSession as _SysSession

from flask import current_app
from ..models import db
from ..utils.commons import fPrint_id_by_time, query_to_dict
from ..utils.response_code import *


class SysSessionManager(_SysSession):
    @classmethod
    def add(cls, **kwargs):
        id = kwargs.get('id')
        data = kwargs.get('data')
        expiry = kwargs.get('expiry')

        filter_list = []
        if id:
            filter_list.append(cls.id == id)
        if data:
            filter_list.append(cls.data == data)
        if expiry:
            filter_list.append(cls.expiry == expiry)

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
                id=id,
                data=data,
                expiry=expiry,
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
        id = kwargs.get('id')
        data = kwargs.get('data')
        expiry = kwargs.get('expiry')

        filter_list = []
        if id:
            filter_list.append(cls.id == id)
        if data:
            filter_list.append(cls.data == data)
        if expiry:
            filter_list.append(cls.expiry == expiry)

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
        id = kwargs.get('id')
        data = kwargs.get('data')
        expiry = kwargs.get('expiry')


        filter_list = []
        if id:
            filter_list.append(cls.id == id)
        if data:
            filter_list.append(cls.data == data)
        if expiry:
            filter_list.append(cls.expiry == expiry)

        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        args = {}
        if id:
            args['id'] = id
        if data:
            args['data'] = data
        if expiry:
            args['expiry'] = expiry

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
        id = kwargs.get('id')
        data = kwargs.get('data')
        expiry = kwargs.get('expiry')

        filter_list = []
        if id:
            filter_list.append(cls.id == id)
        if data:
            filter_list.append(cls.data == data)
        if expiry:
            filter_list.append(cls.expiry == expiry)

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
        id = kwargs.get('id')
        data = kwargs.get('data')
        expiry = kwargs.get('expiry')

        filter_list = []
        if id:
            filter_list.append(cls.id == id)
        if data:
            filter_list.append(cls.data == data)
        if expiry:
            filter_list.append(cls.expiry == expiry)

        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        result = query_to_dict(result_model.all())
        return code_ok(data=result)

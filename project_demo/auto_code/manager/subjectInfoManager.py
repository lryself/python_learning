from ..models.subjectInfoModel import SubjectInfo as _SubjectInfo

from flask import current_app
from ..models import db
from ..utils.commons import fPrint_id_by_time, query_to_dict
from ..utils.response_code import *


class SubjectInfoManager(_SubjectInfo):
    @classmethod
    def add(cls, **kwargs):
        SubjectID = kwargs.get('SubjectID')
        SubjectName = kwargs.get('SubjectName')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if SubjectID:
            filter_list.append(cls.SubjectID == SubjectID)
        if SubjectName:
            filter_list.append(cls.SubjectName == SubjectName)
        if Createtime:
            filter_list.append(cls.Createtime == Createtime)

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
                SubjectID=SubjectID,
                SubjectName=SubjectName,
                Createtime=Createtime,
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
        SubjectID = kwargs.get('SubjectID')
        SubjectName = kwargs.get('SubjectName')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if SubjectID:
            filter_list.append(cls.SubjectID == SubjectID)
        if SubjectName:
            filter_list.append(cls.SubjectName == SubjectName)
        if Createtime:
            filter_list.append(cls.Createtime == Createtime)

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
        SubjectID = kwargs.get('SubjectID')
        SubjectName = kwargs.get('SubjectName')
        Createtime = kwargs.get('Createtime')


        filter_list = []
        if SubjectID:
            filter_list.append(cls.SubjectID == SubjectID)
        if SubjectName:
            filter_list.append(cls.SubjectName == SubjectName)
        if Createtime:
            filter_list.append(cls.Createtime == Createtime)

        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        args = {}
        if SubjectID:
            args['SubjectID'] = SubjectID
        if SubjectName:
            args['SubjectName'] = SubjectName
        if Createtime:
            args['Createtime'] = Createtime

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
        SubjectID = kwargs.get('SubjectID')
        SubjectName = kwargs.get('SubjectName')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if SubjectID:
            filter_list.append(cls.SubjectID == SubjectID)
        if SubjectName:
            filter_list.append(cls.SubjectName == SubjectName)
        if Createtime:
            filter_list.append(cls.Createtime == Createtime)

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
        SubjectID = kwargs.get('SubjectID')
        SubjectName = kwargs.get('SubjectName')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if SubjectID:
            filter_list.append(cls.SubjectID == SubjectID)
        if SubjectName:
            filter_list.append(cls.SubjectName == SubjectName)
        if Createtime:
            filter_list.append(cls.Createtime == Createtime)

        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        result = query_to_dict(result_model.all())
        return code_ok(data=result)

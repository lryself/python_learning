from ..models.classApplyModel import ClassApply as _ClassApply

from flask import current_app
from ..models import db
from ..utils.commons import fPrint_id_by_time, query_to_dict
from ..utils.response_code import *


class ClassApplyManager(_ClassApply):
    @classmethod
    def add(cls, **kwargs):
        AutoID = kwargs.get('AutoID')
        ClassID = kwargs.get('ClassID')
        StudentID = kwargs.get('StudentID')
        Status = kwargs.get('Status')
        IsDelete = kwargs.get('IsDelete')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if ClassID:
            filter_list.append(cls.ClassID == ClassID)
        if StudentID:
            filter_list.append(cls.StudentID == StudentID)
        if Status:
            filter_list.append(cls.Status == Status)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
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
                AutoID=AutoID,
                ClassID=ClassID,
                StudentID=StudentID,
                Status=Status,
                IsDelete=IsDelete,
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
        AutoID = kwargs.get('AutoID')
        ClassID = kwargs.get('ClassID')
        StudentID = kwargs.get('StudentID')
        Status = kwargs.get('Status')
        IsDelete = kwargs.get('IsDelete')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if ClassID:
            filter_list.append(cls.ClassID == ClassID)
        if StudentID:
            filter_list.append(cls.StudentID == StudentID)
        if Status:
            filter_list.append(cls.Status == Status)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
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
        AutoID = kwargs.get('AutoID')
        ClassID = kwargs.get('ClassID')
        StudentID = kwargs.get('StudentID')
        Status = kwargs.get('Status')
        IsDelete = kwargs.get('IsDelete')
        Createtime = kwargs.get('Createtime')


        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if ClassID:
            filter_list.append(cls.ClassID == ClassID)
        if StudentID:
            filter_list.append(cls.StudentID == StudentID)
        if Status:
            filter_list.append(cls.Status == Status)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
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
        if AutoID:
            args['AutoID'] = AutoID
        if ClassID:
            args['ClassID'] = ClassID
        if StudentID:
            args['StudentID'] = StudentID
        if Status:
            args['Status'] = Status
        if IsDelete:
            args['IsDelete'] = IsDelete
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
        AutoID = kwargs.get('AutoID')
        ClassID = kwargs.get('ClassID')
        StudentID = kwargs.get('StudentID')
        Status = kwargs.get('Status')
        IsDelete = kwargs.get('IsDelete')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if ClassID:
            filter_list.append(cls.ClassID == ClassID)
        if StudentID:
            filter_list.append(cls.StudentID == StudentID)
        if Status:
            filter_list.append(cls.Status == Status)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
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
        AutoID = kwargs.get('AutoID')
        ClassID = kwargs.get('ClassID')
        StudentID = kwargs.get('StudentID')
        Status = kwargs.get('Status')
        IsDelete = kwargs.get('IsDelete')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if ClassID:
            filter_list.append(cls.ClassID == ClassID)
        if StudentID:
            filter_list.append(cls.StudentID == StudentID)
        if Status:
            filter_list.append(cls.Status == Status)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
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

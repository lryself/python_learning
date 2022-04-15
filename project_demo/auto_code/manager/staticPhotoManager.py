from ..models.staticPhotoModel import StaticPhoto as _StaticPhoto

from flask import current_app
from ..models import db
from ..utils.commons import fPrint_id_by_time, query_to_dict
from ..utils.response_code import *


class StaticPhotoManager(_StaticPhoto):
    @classmethod
    def add(cls, **kwargs):
        Auto = kwargs.get('Auto')
        photoID = kwargs.get('photoID')
        photoUrl = kwargs.get('photoUrl')

        filter_list = []
        if Auto:
            filter_list.append(cls.Auto == Auto)
        if photoID:
            filter_list.append(cls.photoID == photoID)
        if photoUrl:
            filter_list.append(cls.photoUrl == photoUrl)

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
                Auto=Auto,
                photoID=photoID,
                photoUrl=photoUrl,
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
        Auto = kwargs.get('Auto')
        photoID = kwargs.get('photoID')
        photoUrl = kwargs.get('photoUrl')

        filter_list = []
        if Auto:
            filter_list.append(cls.Auto == Auto)
        if photoID:
            filter_list.append(cls.photoID == photoID)
        if photoUrl:
            filter_list.append(cls.photoUrl == photoUrl)

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
        Auto = kwargs.get('Auto')
        photoID = kwargs.get('photoID')
        photoUrl = kwargs.get('photoUrl')


        filter_list = []
        if Auto:
            filter_list.append(cls.Auto == Auto)
        if photoID:
            filter_list.append(cls.photoID == photoID)
        if photoUrl:
            filter_list.append(cls.photoUrl == photoUrl)

        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        args = {}
        if Auto:
            args['Auto'] = Auto
        if photoID:
            args['photoID'] = photoID
        if photoUrl:
            args['photoUrl'] = photoUrl

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
        Auto = kwargs.get('Auto')
        photoID = kwargs.get('photoID')
        photoUrl = kwargs.get('photoUrl')

        filter_list = []
        if Auto:
            filter_list.append(cls.Auto == Auto)
        if photoID:
            filter_list.append(cls.photoID == photoID)
        if photoUrl:
            filter_list.append(cls.photoUrl == photoUrl)

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
        Auto = kwargs.get('Auto')
        photoID = kwargs.get('photoID')
        photoUrl = kwargs.get('photoUrl')

        filter_list = []
        if Auto:
            filter_list.append(cls.Auto == Auto)
        if photoID:
            filter_list.append(cls.photoID == photoID)
        if photoUrl:
            filter_list.append(cls.photoUrl == photoUrl)

        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        result = query_to_dict(result_model.all())
        return code_ok(data=result)

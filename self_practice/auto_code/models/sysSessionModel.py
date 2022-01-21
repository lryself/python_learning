# coding: utf-8
from . import db


class SysSession(db.Model):
    __tablename__ = 'sys_session'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255, 'utf8mb4_0900_ai_ci'), unique=True)
    data = db.Column(db.LargeBinary)
    expiry = db.Column(db.DateTime, server_default=db.FetchedValue())

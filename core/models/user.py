#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 17:04
# @Author  : qqc
# @File    : User.py
# @Software: PyCharm


from core import db
import datetime


class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # user id
    user_id = db.Column(db.Integer, nullable=False, default=0)
    name = db.Column(db.String(30), unique=True, nullable=False)  # 用户名
    password = db.Column(db.String(128), nullable=False, default='')  # 加盐密码（明文密码长度最大20字符）
    mobile = db.Column(db.String(20), nullable=False, unique=True, default='')  # 手机号码
    remarks = db.Column(db.String(256), nullable=False, default='')  # 个人简介
    state = db.Column(db.SmallInteger, nullable=False, default=0)  # 状态
    create_time = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)
    modify_time = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)


    def get_user_info(self):
        dd = self.__dict__
        dd.pop("_sa_instance_state")
        data = {}
        for k, v in dd.items():
            if isinstance(v, datetime.datetime):
                data[k] = v.strftime('%Y-%m-%d %H:%M:%S')
            else:
                data[k] = v
        return data

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(32), unique=True, nullable=False)
    firstname = db.Column(db.String(32), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(1000), nullable=False)
    birthday= db.Column(db.Date, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    create_time = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)
    modify_time = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)


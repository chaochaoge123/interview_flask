#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 11:10
# @Author  : qqc
# @File    : default.py
# @Software: PyCharm




class Config(object):

    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql://qqc:123456@47.102.138.171/test'


    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = '47.102.138.171'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 10
    CACHE_REDIS_PASSWORD = 'qqcqqc'

    CELERY_BROKER_URL = 'redis://:qqcqqc@47.102.138.171:6379/11'
    CELERY_RESULT_BACKEND = 'redis://:qqcqqc@47.102.138.171:6379/12'
    CELERYD_CONCURRENCY = 16
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_ENABLE_UTC = True
    CELERY_TASK_LOG_LEVEL = 'INFO'
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json', ]
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_IGNORE_RESULT = True
    CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True

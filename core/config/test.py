#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 11:12
# @Author  : qqc
# @File    : test.py
# @Software: PyCharm

import os
from kombu import Exchange
from kombu import Queue
from celery.schedules import crontab

p_path = os.path.abspath(
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        os.pardir, os.pardir))

print('PROJECT_PATH:', p_path)


class TestConfig(object):
    PROJECT_PATH = p_path
    TEMPLATE_FOLDER = os.path.join(PROJECT_PATH, '/templates/')
    STATIC_FOLDER = os.path.join(PROJECT_PATH, '/static/')

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
    CELERY_IMPORTS = (
        'core.tasks.task_one',
    )

    # CELERY_QUEUES = (
    #     Queue('default', Exchange('default', type='direct'), routing_key='default'),
    # )
    # CELERY_DEFAULT_EXCHANGE = 'default'
    # CELERY_DEFAULT_ROUTING_KEY = 'default'
    # CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
    # # CELERY_ROUTES = (QueueRouter(),)
    CELERYBEAT_SCHEDULE = {
        "add_one": {
            "task": "core.tasks.task_one.add_one",
            "schedule": crontab(minute='*/1'),
            "args": ()
        },
    }
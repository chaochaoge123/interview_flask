#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 10:54
# @Author  : qqc
# @File    : task_one.py
# @Software: PyCharm


from core.tasks import celery
import time

__all__ = [
    'add',
    'add_one'
]


@celery.task()
def add(a, b):
    time.sleep(2)
    return a+b


@celery.task()
def add_one():
    time.sleep(2)
    return "this is add_one "
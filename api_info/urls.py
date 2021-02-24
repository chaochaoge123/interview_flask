#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 15:46
# @Author  : qqc
# @File    : urls.py
# @Software: PyCharm

from core import app
from api_info.views import *
from flask import url_for

urls = [
    ('/api/v1', one.test_one),
    ('/api/v1/sql_test', one.test_sql),
    ('/api/v1/orm_test', one.test_orm),
    ('/api/v1/celery_test', one.test_celery),
    ('/api/v1/params_test/<name>', one.test_params),
    ('/api/v1/template_test/<name>', one.test_template),
]

urls += [
    ('/api/v1/index', one.index),
    ('/v1/user/one/chet/templates', one.user_one_templates),
    ('/v1/student/save', one.student_save, ["POST"]),
    ('/v1/student/search', one.student_search),

]

for url in urls:
    app.add_url_rule(url[0], view_func=url[1], methods=url[-1] if isinstance(url[-1], list) else ["GET"])


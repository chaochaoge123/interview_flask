#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 10:13
# @Author  : qqc
# @File    : chet_url.py
# @Software: PyCharm

from core import app
from api_info.views import *
from flask import url_for

urls = [
    ('/ws/v1/user/one/chet/<username>', ws_view.user_chet_ws),
    ('/ws/v1/user/all/chet/<username>', ws_view.user_all_chet_ws),

]

for url in urls:
    app.add_url_rule(url[0], view_func=url[-1])

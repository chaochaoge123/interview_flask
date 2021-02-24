#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 17:27
# @Author  : qqc
# @File    : error_code.py
# @Software: PyCharm


class ErrorCode(object):
    API_REQUESTS_SUCCESS = ("10000", '成功')
    API_PARAMS_ERROR = ("10001", 'API参数缺失或错误')
    API_NOT_USER_ERROR = ("10002", '用户不存在')
    API_SERVER_ERROR = ("10003", '服务错误')
    API_MSG_TYPE_ERROR = ("10004", '消息类型错误')
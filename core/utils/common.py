#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 15:20
# @Author  : qqc
# @File    : sql_tool.py
# @Software: PyCharm


from core import db
from flask import make_response
import json
from core.utils.error_code import *
import requests

def run_sql(sql_text):
    try:
        cursor = db.session
        res_rows = cursor.execute(sql_text)
        cursor.commit()
        return [dict(zip(result.keys(), result)) for result in res_rows]
    except Exception as e:
        print(e)
        return []
    finally:
        db.session.close()


def api_response(data=None, error=None):
    res = {}
    if data is not None:
        res["data"] = data
        res['code'] = ErrorCode.API_REQUESTS_SUCCESS[0]
        res["message"] = ErrorCode.API_REQUESTS_SUCCESS[1]
    if error is not None:
        res['data'] = {}
        res['code'] = error[0]
        res["message"] = error[1]
    return make_response(res)


import time
def is_valid_date(D_str):
    try:
        time.strptime(D_str, '%Y-%m-%d')
        print('t')
        return True
    except:
        print('f')
        return False


def search_username(username):
    url = 'http://172.30.4.154:9200/index_user/_search'
    params = {
        "query": {
            "wildcard": {
                "name": {
                    "value": "*{0}*".format(username)
                }
            }
        }
    }
    user_data = requests.post(url, json=params)
    return user_data.json()

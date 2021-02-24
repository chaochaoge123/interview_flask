#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 15:53
# @Author  : qqc
# @File    : one.py
# @Software: PyCharm

from core.utils.common import *
from core.models import *
from core.utils.error_code import *
from flask import request, render_template,session
from core.tasks.task_one import *
from markupsafe import escape
from core import app, db
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)
def test_one():
    return {"age": 66}


def test_sql():
    res = run_sql("select * from user_info")
    print(res)
    return "successful"


def test_orm():
    try:
        user_id=int(request.args.get('user_id'))
    except:
        return api_response(error=ErrorCode.API_PARAMS_ERROR)
    info = UserInfo.query.filter_by(id=user_id).first()
    if not info:
        return api_response(error=ErrorCode.API_NOT_USER_ERROR)
    data = info.get_user_info()
    print(data)
    return api_response(data=data)


def test_celery():
    num=add.delay(50,50)
    return api_response(data={})


def test_params(name):
    print(request.method, "#############")
    print(escape(name),"CCCCCCCCCCCCCCC")
    print(session,"DDDDDDDDDDD",app.secret_key)
    return api_response(data={"name":name})


def test_template(name):
    return render_template('one.html', name=name)


def index():
    pass

def user_one_templates():
    return render_template('dl.html')


def student_save():
    user_data = request.json
    print(user_data, "$######################")
    username = user_data.get('username', '')
    firstname = user_data.get('firstname', '')
    lastname = user_data.get('lastname', '')
    address = user_data.get('address', '')
    description = user_data.get('description', '')
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    birthday = user_data.get('birthday', '')
    if not username or not username.islower() or len(username) < 4:
        return api_response(error=(70005, "More than 4 characters lower case"))
    if len(firstname) > 20:
        return api_response(error=(70006, "Required, less than 20 characters"))
    if not is_valid_date(birthday):
        return api_response(error=(70007, "Date type: YYYY-MM-DD"))

    if not user_data.get('id'):
        insert_sql = """ insert into test.student (username,firstname,lastname,address,birthday,description,create_time) values 
        ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')""".format(username, firstname, lastname, address, birthday, description,
                                                create_time)
        print(insert_sql, "&&&&&&&&&&&&&&&&&&&")
        run_sql(insert_sql)
    else:
        id = user_data.get('id')
        update_sql = """ update test.student set username='{0}',firstname='{1}',lastname='{2}',address='{3}',birthday='{4}',
        description='{5}' where id={6}""".format(username, firstname, lastname, address, birthday, description, id)
        print(update_sql, "*********************************")
        run_sql(update_sql)
    return api_response(data={})


def student_search():
    username = request.args.get('username', '')
    if not username:
        return api_response(error=(80001, "不能为空"))
    url = 'http://172.30.4.154:9200/index_student/_search'
    params = {
        "query": {
            "wildcard": {
                "username": {
                    "value": "*{0}*".format(username)
                }
            }
        }
    }
    user_data = requests.post(url, json=params)
    return api_response(data=user_data.json())

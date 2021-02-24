#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 10:14
# @Author  : qqc
# @File    : chet_view.py
# @Software: PyCharm

from flask import render_template,request
from geventwebsocket.exceptions import WebSocketError
from core.utils.common import *
from core.models import *
from core.utils.error_code import *
from core.tasks.task_one import *
from markupsafe import escape
from core import app

user_socket_dict = {}


def user_chet_ws(username):
    print(request.url,"GGGGGGGGG")
    print(request.args,"AAAAAAAAAAAAAAAAAAAAAAAAA",request.headers)

    msg_type=request.args.get('msg_type')


    user_socket = request.environ.get("wsgi.websocket")
    if not user_socket:
        return api_response(error=ErrorCode.API_SERVER_ERROR)

    if username not in user_socket_dict:
        user_socket_dict[username] = user_socket
    print("在线用户%s" % user_socket_dict)

    while True:
        try:
            user_msg = user_socket.receive()
            print("接收到的信息", user_msg)
            if user_msg is None:
                print("%s 已下线" % username)
                user_socket_dict.pop(username)
            else:
                user_msg = json.loads(user_msg)
                if int(msg_type) == 1:
                    to_user_socket = user_socket_dict.get(user_msg.get("to_user"))
                    send_msg = {
                        "send_msg": user_msg.get("send_msg"),
                        "send_user": username
                    }
                    to_user_socket.send(json.dumps(send_msg))
                elif int(msg_type)==2:
                    pass
                else:
                    return api_response(ErrorCode.API_MSG_TYPE_ERROR)
        except WebSocketError:
            pass
        return api_response()


group_user_dict={}
def user_all_chet_ws(username):
    user_socket = request.environ.get("wsgi.websocket")
    if not user_socket:
        return api_response(error=ErrorCode.API_SERVER_ERROR)

    if username not in group_user_dict:
        group_user_dict[username] = user_socket
    print("在线用户%s" % group_user_dict)

    while True:
        try:
            user_msg = user_socket.receive()
            if user_msg is None:
                print("%s 已下线" % username)
                group_user_dict.pop(username)
            for user_name, u_socket in group_user_dict.items():

                who_send_msg = {
                    "send_user": username,
                    "send_msg": user_msg
                }
                print(who_send_msg, "################")
                if user_socket == u_socket or user_msg is None:
                    continue
                u_socket.send(json.dumps(who_send_msg))

        except WebSocketError:
            pass
        return api_response()

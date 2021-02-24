#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 10:11
# @Author  : qqc
# @File    : websocket_server.py
# @Software: PyCharm

from core import app
from flask import Flask, request, render_template
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
import os
from api_info import *

if __name__ == '__main__':
    print('服务启动')
    print(os.environ, "#######################")
    http_server = WSGIServer(('127.0.0.1', 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
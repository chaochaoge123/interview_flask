#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 14:33
# @Author  : qqc
# @File    : send.py
# @Software: PyCharm

import pika
import sys

# https://www.rabbitmq.com/tutorials/tutorial-three-python.html

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters(host='172.30.4.154', port=5672, credentials=credentials, virtual_host='my_vhost')
connection = pika.BlockingConnection(parameters)

# 队列连接通道
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()
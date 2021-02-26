#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 15:07
# @Author  : qqc
# @File    : send.py
# @Software: PyCharm

import pika
import sys

# https://www.rabbitmq.com/tutorials/tutorial-four-python.html

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters(host='172.30.4.154', port=5672, credentials=credentials, virtual_host='my_vhost')
connection = pika.BlockingConnection(parameters)

# 队列连接通道
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
print("severity....%s" % severity)
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange='direct_logs', routing_key=severity, body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()


# python3 send.py error  发送日志时，指定类型
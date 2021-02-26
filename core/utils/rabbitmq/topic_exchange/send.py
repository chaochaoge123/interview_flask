#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 15:40
# @Author  : qqc
# @File    : send.py
# @Software: PyCharm

import pika
import sys

# https://www.rabbitmq.com/tutorials/tutorial-five-python.html

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters(host='172.30.4.154', port=5672, credentials=credentials, virtual_host='my_vhost')
connection = pika.BlockingConnection(parameters)

# 队列连接通道
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange='topic_logs', routing_key=routing_key, body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()
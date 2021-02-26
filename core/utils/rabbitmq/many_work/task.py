#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 13:47
# @Author  : qqc
# @File    : task.py
# @Software: PyCharm

import pika
import sys

# https://www.rabbitmq.com/tutorials/tutorial-two-python.html

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters(host='172.30.4.154', port=5672, credentials=credentials, virtual_host='my_vhost')
connection = pika.BlockingConnection(parameters)

# 队列连接通道
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()
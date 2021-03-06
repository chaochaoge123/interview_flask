#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/24 15:30
# @Author  : qqc
# @File    : send.py
# @Software: PyCharm

import pika

# https://www.rabbitmq.com/tutorials/tutorial-one-python.html

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters(host='172.30.4.154', port=5672, credentials=credentials, virtual_host='my_vhost')
connection = pika.BlockingConnection(parameters)

# 队列连接通道
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='this one message')
print(" [x] Sent 'Hello World!'")
connection.close()

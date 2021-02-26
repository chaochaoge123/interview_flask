#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 14:42
# @Author  : qqc
# @File    : receive.py
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

result = channel.queue_declare(queue='', exclusive=True)  # 随机命名队列，连接关闭时清除改队列
queue_name = result.method.queue
print(queue_name, "################")

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

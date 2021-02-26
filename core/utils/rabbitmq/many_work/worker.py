#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 13:49
# @Author  : qqc
# @File    : worker.py
# @Software: PyCharm

import pika
import time

# https://www.rabbitmq.com/tutorials/tutorial-two-python.html

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters(host='172.30.4.154', port=5672, credentials=credentials, virtual_host='my_vhost')
connection = pika.BlockingConnection(parameters)
# 队列连接通道
channel = connection.channel()


channel.queue_declare(queue='task_queue', durable=True) # durable=True持久化队列
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)  # 公平分发
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
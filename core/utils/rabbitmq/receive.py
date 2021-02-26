#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/24 15:30
# @Author  : qqc
# @File    : reveice.py
# @Software: PyCharm

import pika, sys, os

def main():
    credentials = pika.PlainCredentials('admin', 'admin')
    parameters = pika.ConnectionParameters(host='172.30.4.154', port=5672, credentials=credentials, virtual_host='my_vhost')
    # virtual_host 类似于mysql的db,指定用户访问那个db
    connection = pika.BlockingConnection(parameters)

    # 队列连接通道
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        print({"ch":ch,"method":method,"properties":properties},"GGGGGGGGGGGGGGGGG")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
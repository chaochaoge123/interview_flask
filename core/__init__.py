#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from core.config import config
from flask_sqlalchemy import SQLAlchemy
import redis

def create_app():
    """
    Create flask app.
    """

    _app = Flask(__name__)

    _app.config.from_object(config)

    _app.template_folder = _app.config['TEMPLATE_FOLDER']

    _app.static_folder = _app.config['STATIC_FOLDER']

    return _app

app = create_app()

db = SQLAlchemy(app)

pool = redis.ConnectionPool(host=app.config['CACHE_REDIS_HOST'], port=app.config['CACHE_REDIS_PORT'],
                            password=app.config['CACHE_REDIS_PASSWORD'], db=app.config['CACHE_REDIS_DB'],
                            max_connections=500)
redis_cache = redis.StrictRedis(connection_pool=pool)

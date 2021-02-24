#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 15:06
# @Author  : qqc
# @File    : add_signals.py
# @Software: PyCharm


from blinker import Namespace

_signals = Namespace()

saved = _signals.signal('model_saved')


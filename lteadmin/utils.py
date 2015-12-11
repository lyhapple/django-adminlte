#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

__author__ = 'lyhapple'


def format_datetime(datetime, format_str='%Y-%m-%d %H:%M:%S'):
    return datetime.strftime(format_str)
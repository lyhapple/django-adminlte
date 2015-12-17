#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from datetime import datetime
from django import template
from django.db.models import ImageField
from lteadmin import utils

__author__ = 'lyhapple'


register = template.Library()


def get_attr(obj, attr_name):
    """
    当attr_name中包含'.'时，获取属性值
    :param obj:
    :param attr_name:
    :return:
    """
    if '.' in attr_name:
        lst_attr = [obj]
        lst_attr.extend(attr_name.split('.'))
        return reduce(getattr, lst_attr)
    else:
        return getattr(obj, attr_name)


@register.filter(name='render_field_label')
def render_field_label(obj, field_name):
    if '.' in field_name:
        field_name = field_name.split('.', 1)[0]
    if hasattr(obj, field_name):
        meta_fields = obj._meta.fields
        for mf in meta_fields:
            if mf.name == field_name:
                return mf.verbose_name
        return u'未知'
    else:
        return u''


@register.filter(name='render_field_value')
def render_field_value(obj, a):
    value = '-'
    if hasattr(obj, a) or '.' in a:
        value = get_attr(obj, a)
        if value is None:
            value = '-'
        else:
            if hasattr(value, 'field'):
                if isinstance(value.field, ImageField) and value:
                    value = "<img src='%s' />" % value.url
                else:
                    value = '<img src="%s" alt="求真相" />'
            elif hasattr(obj, 'get_%s_display' % a):
                value = getattr(obj, 'get_%s_display' % a)()
            elif isinstance(value, datetime):
                value = utils.format_datetime(value)
    return value

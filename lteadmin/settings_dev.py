#!/usr/bin/env python
# -*- coding: utf-8 -*-

from settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'logs', 'dev_db.sqlite3'),
    }
}

############################################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,# this fixes the problem
    'formatters': {
        'standard': {#详细
            'format': LOGGING_stamdard_format
        },
        'simple': {#简单
            'format': LOGGING_simple_format
        },
        'request': {#简单
            'format': LOGGING_request_format
        },
    },
    'filters': {},
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console':{
            'level': 'INFO',
            'class': 'logging.StreamHandler',#打印到前台
            'formatter': 'simple'
        },
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR+'/logs/','dev_all.log'), #或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024*1024*10, # 10 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'request': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR+'/logs/','dev_request.log'), #或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024*1024*10, # 10 MB
            'backupCount': 5,
            'formatter':'request',
        },
        'db': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR+'/logs/','dev_db.log'), #或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024*1024*10, # 10 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'scprits_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR+'/logs/','dev_scprits.log'), #或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024*1024*10, # 10 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'web_api': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR+'/logs/','dev_web_api.log'), #或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024*1024*10, # 10 MB
            'backupCount': 5,
            'formatter':'simple',
        },
        'web_manage': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR+'/logs/','dev_web_manage.log'), #或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024*1024*10, # 10 MB
            'backupCount': 5,
            'formatter':'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default','console'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['request','default'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'scripts': { # 脚本专用日志
            'handlers': ['scprits_handler','default','console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'web_api': { # 脚本专用日志
            'handlers': ['web_api','default','console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'web_manage': { # 脚本专用日志
            'handlers': ['web_manage','default','console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.db.backends':{
            'handlers': ['db'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
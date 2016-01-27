#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
For CentOS 7
"""

from __future__ import absolute_import, print_function, unicode_literals
from fabric.context_managers import cd, prefix
from fabric.operations import sudo
from fabric.state import env

__author__ = 'lyhapple'


# replace user@host
env.hosts = ['user@host']

# your host password
env.password = ''

DEPLOY_ROOT = '/data/deploy'

LOGS_ROOT = '%s/logs' % DEPLOY_ROOT

NGINX_LOGS_ROOT = '%s/nginx' % LOGS_ROOT

VIRTUAL_ROOT = '%s/console' % DEPLOY_ROOT

WEB_ROOT = '%s/web' % VIRTUAL_ROOT

ACTIVATE = 'source %s/bin/activate' % VIRTUAL_ROOT

PROJECT_GIT = 'git@github.com:lyhapple/django-adminlte.git'


def init_server():
    sudo('sudo yum install -y nginx python-pip supervisor mysql mysql-devel')
    sudo('pip install virtualenv uwsgi gunicorn')
    sudo('mkdir -p %s' % DEPLOY_ROOT)


def init_env():
    with cd(DEPLOY_ROOT):
        sudo('virtualenv console')
    sudo('mkdir -p %s' % WEB_ROOT)
    sudo('mkdir -p %s' % LOGS_ROOT)
    sudo('mkdir -p %s' % NGINX_LOGS_ROOT)


def clone_data():
    with cd(WEB_ROOT):
        sudo('git clone %s web' % PROJECT_GIT)
        sudo('cd web')
        sudo('git checkout develop')


def restart():
    sudo('systemctl restart nginx')
    sudo('killall -9 uwsgi')
    sudo('uwsgi --ini %s/conf/uwsgi.ini' % WEB_ROOT)


def init_console():
    with cd(WEB_ROOT):
        with prefix(ACTIVATE):
            sudo('pip install -r requirements.txt')
            sudo('python manage.py migrate')
            sudo('python manage.py loaddata conf/fixture_data.json')
            sudo('python manage.py collectstatic --noinput')
            # todo:lyh:modify /etc/nginx/nginx.conf
            sudo('cp conf/adminlte.conf /etc/nginx/conf.d/')


def update():
    with cd(WEB_ROOT):
        with prefix(ACTIVATE):
            sudo('git pull origin develop')
            sudo('pip install -r requirements.txt')
            sudo('python manage.py migrate')
            # sudo('python manage.py collectstatic')
            restart()

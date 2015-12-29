#!/bin/bash
cd `dirname $0`
BIN_DIR=`pwd`
PYTHON=`which python`
ps aux |grep $BIN_DIR/manage.py |grep -v grep |awk '{print $2}'|xargs kill -9
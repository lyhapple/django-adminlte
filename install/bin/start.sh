#!/bin/bash
cd `dirname $0`
BIN_DIR=`pwd`
PYTHON=`which python`
nohup $PYTHON $BIN_DIR/manage.py runserver 0.0.0.0:8080 &
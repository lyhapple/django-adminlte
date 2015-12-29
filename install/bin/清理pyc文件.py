#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
def del_files(path):
  for root , dirs, files in os.walk(path):
    for name in files:
      if name.endswith(".pyc"):
        os.remove(os.path.join(root, name))
        print ("Delete File: " + os.path.join(root, name))
# test
if __name__ == "__main__":
  path = 'C:\\Users\\xuebk\\Documents\\gz\\CMDB\\cmdbdemo_online_gz'
  del_files(path)
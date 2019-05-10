#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
   for i in range(1,10,2):
       print('我是子进程：',i)
else:
    for i in range(0,10,2):
        print('我是父进程：',i)

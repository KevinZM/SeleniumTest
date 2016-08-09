# -*- coding:utf-8 -*-
import runpy
import time

# runpy.run_path('登录.py')
execfile('登录.py')
time.sleep(2)

execfile('登出.py')
time.sleep(2)

execfile('添加主机.py')
time.sleep(2)

execfile('添加共享数据存储域.py')
time.sleep(2)

execfile('添加ISO存储域.py')
time.sleep(2)

execfile('添加exports存储域.py')

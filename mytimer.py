# env       ：Python v 3.7.3
# -*- coding：utf-8 -*-
# @Time     ：2019/10/21 15:00
# @Author   ：Jason Phillip
# @File     ：mytimer.py

#通用计时器工具函数

import time
reps = 1000
repslist = range(reps)

def timer(func,*pargs,**kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs,**kargs)
    elapsed = time.clock() - start
    return (elapsed,ret)
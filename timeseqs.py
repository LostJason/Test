# env       ：Python v 3.7.3
# -*- coding：utf-8 -*-
# @Time     ：2019/10/21 15:03
# @Author   ：Jason Phillip
# @File     ：timeseqs.py

import sys,mytimer

reps = 10000
repslist = range(reps)

def forloop():
    res= []
    for x in repslist:
        res.append((abs(x)))
    return  res

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return  list(map(abs,repslist))

def genExpr():
    return list(abs(x) for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())

print(sys.version)
for test in (forloop(),listComp(),mapCall(),genExpr(),genFunc()):
    elapsed,result = mytimer.timer(test)
    print('-'*33)
    print('%-9s:%.5f => [%s...%s]' %
          (test.__name__,elapsed,result[0],result[-1]))

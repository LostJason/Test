# env       ：Python v 3.7.3
# -*- coding：utf-8 -*-
# @Time     ：2019/10/20 22:42
# @Author   ：Jason Phillip
# @File     ：FirstFile.py
# https://docs.python.org/zh-cn/3.7/library/turtle.html?highlight=turtle#turtle.ontimer

import turtle as t

t.setup(800, 600, 0, 0)
t.color('red', 'black')

t.shape(name='classic')
t.mode('logo')
# 绘制表面
t.tracer(10, 1000)
for i in range(60):
    if i % 5:
        t.pencolor('white')
        t.fd(210)
        t.pensize(width=2)
        t.pencolor('black')
        t.fd(10)
        t.penup()
        t.home()
        t.pendown()
        t.setheading(i * 6 + 6)
    else:
        t.pencolor('white')
        t.fd(200)
        t.pensize(width=5)
        t.pencolor('black')
        t.fd(20)
        if i == 0:
            t.write('12', font=('微软雅黑', 16))
        else:
            t.fd(10)
            t.write(str(i // 5), font=('微软雅黑', 16))
        t.penup()
        t.home()
        t.pendown()
        t.setheading(i * 6 + 6)


# 绘制时针
def drw_hor():
    for i in range(60):
        t.color('black')
        t.pencolor('white')
        t.fd(200)
        t.stamp()
        t.penup()
        t.home()
        t.pendown()
        t.setheading(i * 6 + 6)
    t.clearstamps(None)


# 绘制分针
def drw_min():
    t.color('black')
    t.pensize(3)
    t.fd(100)
    t.penup()
    t.home()
    t.pendown()
    t.setheading(i * 6 + 6)


# 绘制秒针
def drw_sec():
    for i in range(60):
        if t.stamp():
            t.clearstamps(None)
        t.color('black')
        t.pencolor('white')
        t.fd(200)
        t.stamp()
        t.penup()
        t.ontimer(t.home(), 100)
        t.pendown()
        t.setheading(i * 6 + 6)
    t.clearstamps(None)


# 计时
for i in range(2):
    drw_min()
    drw_sec()
    drw_min()

t.done()




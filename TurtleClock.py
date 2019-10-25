# env       ：Python v 3.7.3
# -*- coding：utf-8 -*-
# @Time     ：2019/10/20 22:42
# @Author   ：Jason Phillip
# @File     ：TurtleClock.py
# https://docs.python.org/zh-cn/3.7/library/turtle.html?highlight=turtle#turtle.ontimer

import turtle
from datetime import *


def create_Shape_Hand(name, length):
    turtle.reset()
    turtle.begin_poly()
    turtle.penup()
    turtle.fd(length)
    turtle.hideturtle()
    turtle.end_poly()
    turtle.register_shape(name, turtle.get_poly())


def create_Shape_Clock(name, length, heigth):
    turtle.reset()
    turtle.pensize(5)
    turtle.penup()
    turtle.fd(length)
    turtle.pendown()
    turtle.begin_poly()
    turtle.fd(heigth)
    turtle.hideturtle()
    turtle.end_poly()
    turtle.register_shape(name, turtle.get_poly())


def setup_Hand():
    global mz, fz, sz
    create_Shape_Hand('miaozhen', 200)
    create_Shape_Hand('fenzhen', 180)
    create_Shape_Hand('shizhen', 120)
    mz = turtle.Turtle()
    fz = turtle.Turtle()
    sz = turtle.Turtle()
    mz.shape('miaozhen')
    fz.shape('fenzhen')
    sz.shape('shizhen')


# 乌龟返回原点，不画线
def backorigin():
    turtle.penup()
    turtle.home()
    turtle.pendown()


# 乌龟前进指定长度， 但不画线
def drw_null(x):
    turtle.penup()
    turtle.fd(x)
    turtle.pendown()


# 画表盘线并标记数字
def drw_clock(x, y, z, m):
    drw_null(x)
    turtle.pensize(width=z)
    turtle.fd(y)
    ddd(m)
    backorigin()


# 画表盘外圆
def setup_circle(x):
    turtle.penup()
    turtle.goto(x, 0)
    turtle.pendown()
    turtle.circle(x)


# 调整表盘数字位置
def ddd(h):
    if 60 > turtle.heading() >= 0:
        turtle.write(str(h), align="center", font=('微软雅黑', 16, "bold"))
    elif 120 > turtle.heading() >= 60:
        drw_null(15)
        turtle.write(str(h), align="center", font=('微软雅黑', 16, "bold"))
    elif 180 > turtle.heading() >= 120:
        drw_null(30)
        turtle.write(str(h), align="center", font=('微软雅黑', 16, "bold"))
    elif 360 > turtle.heading() >= 300:
        turtle.write(str(h), align="center", font=('微软雅黑', 16, "bold"))
    elif 300 > turtle.heading() >= 240:
        drw_null(15)
        turtle.write(str(h), align="center", font=('微软雅黑', 16, "bold"))
    elif 240 > turtle.heading() >= 180:
        drw_null(30)
        turtle.write(str(h), align="center", font=('微软雅黑', 16, "bold"))
    # 创建表


def setup_Clock():
    for i in range(60):
        if i == 0 or i == 30:
            drw_clock(200, 20, 4, i)
            turtle.setheading(i * 6 + 6)
        elif i == 5 or i == 15 or i == 25:
            drw_clock(200, 20, 2, i)
            turtle.setheading(i * 6 + 6)
        elif i == 10 or i == 20:
            drw_clock(200, 20, 4, i)
            turtle.setheading(i * 6 + 6)
        elif i == 35 or i == 45 or i == 55:
            drw_clock(200, 20, 2, i)
            turtle.setheading(i * 6 + 6)
        elif i == 40 or i == 50:
            drw_clock(200, 20, 4, i)
            turtle.setheading(i * 6 + 6)
        else:
            drw_clock(205, 15, 1, '')
            turtle.setheading(i * 6 + 6)
    setup_circle(220)
    setup_circle(250)


def date(t):
    week = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    w = week[turtle.weekday()]
    return '%s年%s月%s日\n%s时%s分%s秒\n%s' % (
    turtle.year, turtle.month, turtle.day, turtle.hour, turtle.minute, turtle.second, w)


def run_Clock():
    t = datetime.today()
    mz.setheading(6 * (t.second + t.microsecond * 0.000001))
    fz.setheading(6 * t.minute)
    sz.setheading(30 * t.hour)
    turtle.ontimer(run_Clock, 10)


def main():
    turtle.mode('logo')
    setup_Hand()
    turtle.tracer(False)
    setup_Clock()
    turtle.tracer(True)
    run_Clock()
    turtle.mainloop()


if __name__ == "__main__":
    main()
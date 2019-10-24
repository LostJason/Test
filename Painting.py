# env       ：Python v 3.7.3
# -*- coding：utf-8 -*-
# @Time     ：2019/10/22 15:13
# @Author   ：Jason Phillip
# @File     ：Painting.py

import turtle as t
#设置画布，起始位置
t.screensize(200,150,'white')
t.setup(800,600,0,0)
#t.speed(10)

def set_coordinate(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#绘制坐标系
def dw_pos():
    coor = set_coordinate
    coor(0,-200)
    t.left(90)
    t.fd(400)
    t.begin_fill()
    t.right(150)
    t.fd(10)
    t.right(120)
    t.fd(10)
    t.right(120)
    t.fd(10)
    t.end_fill()

    coor(-300,0)
    t.setheading(0)
    t.fd(600)
    t.begin_fill()
    t.right(150)
    t.fd(10)
    t.right(120)
    t.fd(10)
    t.right(120)
    t.fd(10)
    t.end_fill()
    t.hideturtle()
dw_pos()

#绘制y = x**2 的图形

#绘制心形1
def drw_heart1(x,y,z,o):
    t.setheading(o)
    for i in range(x):
        t.right(y)
        t.fd(z)
def drw_heart2(x,y,z,o):
    t.setheading(o)
    for i in range(x):
        if y>0:
            t.left(y+(i/4))
        else:
            t.left(y-(i/4))
        t.fd(z)

t.color('red','red')
t.begin_fill()
t.penup()
t.setpos(0,100)
t.pendown()
drw_heart1(119,-1,1,120)
drw_heart2(11,10,21,242)

t.penup()
t.setpos(0,100)
t.pendown()
drw_heart1(119,1,1,60)
drw_heart2(11,-10,21,-62)
t.end_fill()



t.done()




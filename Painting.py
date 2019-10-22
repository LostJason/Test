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
coor = set_coordinate
#绘制坐标系
coor(-200,0)
t.fd(400)
coor(0,-200)
t.left(90)
t.fd(400)
#绘制圆
coor(100,0)
t.circle(100)

#绘制y = x**2 的图形
def yx(a):
    for x in range(-10,11):
        y = x ** a
        coor(x,y)
        t.dot(2,'red')
yx(2)
t.hideturtle()
t.done()
#
# t.color('red','yellow')
# t.speed(1)
# t.fd(100)
# #t.left(10)
# t.dot(10,'blue')
# t.penup()
# t.goto(10,10)
# t.write('Python 牛B')



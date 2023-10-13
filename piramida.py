from turtle import *

drawing_area = Screen()
drawing_area.setup(width=750, height=500)

speed(0)

def brick(a, b):
    for i in range(2):
        fd(a)
        right(90)
        fd(b)
        right(90)

def row(n):
    for i in range(n):
        brick(20,10)
        pen(up)
        fd(20)
        pen(down)

def piramid(c):
    for i in range(c):
        row(c-i)
        right(180)
        fd((c-i)*20-10)
        right(90)
        penup()
        fd(10)
        pendown()
        right(90)


piramid(9)





done()
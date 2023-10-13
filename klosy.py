from turtle import *

drawing_area = Screen()
drawing_area.setup(width=1000, height=700)

speed(0)

penup()
bk(350)
pendown()

def ziarnol(a):
        fd(a)
        left(45)
        fd(2*a)
        left(45)
        fd(a)
        right(45)
        fd(a)
        bk(a)
        left(45)
        left(90)
        fd(a)
        left(45)
        fd(2*a)
        left(45)
        fd(a)
        left(90)

def ziarnor(a):
        fd(a)
        rt(45)
        fd(2*a)
        rt(45)
        fd(a)
        lt(45)
        fd(a)
        bk(a)
        rt(135)
        fd(a)
        rt(45)
        fd(2*a)
        rt(45)
        fd(a)
        rt(90)

def kls(n):
        fd(500)
        bk(250)
        for i in range(n):
                ziarnol(125/n)
                fd(250/n)
        rt(45)
        ziarnol(125/n)
        lt(45)
        bk(250)
        for i in range(n):
                ziarnor(125/n)
                fd(250/n)




kls(100)

done()

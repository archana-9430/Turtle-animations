import turtle
from random import randint

hi = turtle.Turtle()
s = turtle.Screen()
hi.speed(0)
s.bgcolor("black")
x = 1

def flower(x: int, y: int, z:int, rotation: int):
    hi.up()
    hi.goto(y, z)
    hi.down()
    hi.width(4)
    while x < rotation:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        turtle.colormode(255)
        hi.pencolor(r, g, b)
        hi.fd(x)
        hi.rt(306)
        x += 1

#flower(-70, 10, 180, 130)
x=1
flower(-50, -210, 130, 92)
hi.up()
hi.speed(3)
hi.goto(-215, 0)
hi.down()
#hi.setheading(-5)
hi.circle(300, 80)


turtle.done()    
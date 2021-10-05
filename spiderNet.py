import turtle
from random import randint

hi = turtle.Turtle()
s = turtle.Screen()
hi.speed(0)
s.bgcolor("black")
x = 1
hi.up()
hi.goto(10, 10)
hi.down()
hi.width(4)
while x < 205:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turtle.colormode(255)
    hi.pencolor(r, g, b)
    hi.fd(10 + x)
    hi.rt(36)
    x += 1

turtle.done()    
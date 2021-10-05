import turtle
from random import randint

hi = turtle.Turtle()
s = turtle.Screen()
hi.speed(0)
s.bgcolor("black")
x = 1
hi.up()
hi.goto(10, -270)
hi.down()
hi.width(2)
while x < 301:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turtle.colormode(255)
    hi.pencolor(r, g, b)
    hi.circle(x)
    x += 2

turtle.done()    
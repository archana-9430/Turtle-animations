import turtle
from random import randint

hi = turtle.Turtle()
hi.hideturtle()
s = turtle.Screen()
hi.speed(0)
s.bgcolor("black")
x = 1
hi.up()
hi.goto(10, 15)
hi.down()
hi.width(2)
while x < 401:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turtle.colormode(255)
    hi.pencolor(r, g, b)
    hi.fd(50 + x)
    hi.rt(90.911)
    x += 1

turtle.done()    
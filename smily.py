import turtle
hi = turtle.Turtle()
hi.color("orange")
s = turtle.Screen()
hi.speed(0.4)
s.bgcolor("black")
hi.up()
hi.goto(300,-230)
hi.down()
hi.circle(100)




hi.fillcolor("yellow")
hi.begin_fill()
hi.setheading(360)
hi.up()
hi.goto(300,-230)
hi.down()
hi.circle(100)
hi.end_fill()
turtle.done()
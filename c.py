import turtle

hi = turtle.Turtle()

s = turtle.Screen()
s.bgcolor("black")
hi.width(5)
hi.speed(1)
hi.hideturtle()
###########A#################
def draw_A(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.goto(x, y)
    hi.down()
    hi.setheading(70)
    hi.fd(200)
    hi.bk(100)
    hi.setheading(360)
    hi.fd(69)
    hi.setheading(110)
    hi.fd(100)
    hi.bk(200)

##########################

def draw_a(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.goto(x, y);
    hi.down()
    hi.circle(-24, 180)
    hi.setheading(270)
    hi.fd(40)
    hi.circle(10, 90)
    hi.up()
    hi.goto(x + 48, y)
    hi.down()
    hi.setheading(210)
    hi.fd(20)
    hi.circle(45, 70)
    hi.setheading(354)
    hi.circle(80, 32)

#################################

################################

def draw_C(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.goto(x, y)
    hi.down()
    hi.setheading(90)
    hi.circle(30, 180)
    hi.fd(50)
    hi.circle(30, 180)

#################################
def D(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.goto(x, y)
    hi.down()
    hi.setheading(90)
    hi.fd(100)
    hi.setheading(360)
    hi.circle(-50, 90)
    hi.circle(-50, 90)

#############################

def E(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.goto(x, y)
    hi.down()
    hi.setheading(180)
    hi.fd(50)
    hi.setheading(270)
    hi.fd(100)
    hi.setheading(360)
    hi.fd(50)
    hi.up()
    hi.goto(x - 50, y-50)
    hi.down()
    hi.setheading(360)
    hi.fd(50)

#############################
#############################
#############################


def H(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.color("blue")
    hi.up()
    hi.goto(x, y)
    hi.down()
    hi.setheading(90)
    hi.bk(100)
    hi.fd(50)
    hi.setheading(360)
    hi.fd(50)
    hi.setheading(90)
    hi.fd(50)
    hi.bk(100)

########################
##############################
###############################
############################

def draw_O(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.goto(x, y)
    hi.setheading(360)
    hi.down()
    hi.circle(35, 90)
    hi.fd(100)
    hi.circle(35, 180)
    hi.fd(100)
    hi.circle(35, 90)

########################

def p(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.goto(x, y)
    hi.down()
    hi.setheading(270)
    hi.fd(100)
    hi.bk(70)
    hi.setheading(360)
    hi.circle(-30, 180)

#############################

def P(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.goto(x, y)
    hi.setheading(90)
    hi.down()
    hi.fd(80)
    hi.circle(-20, 180)
    hi.fd(20)
    hi.circle(-20, 180)

#################################
#############################

def R(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.goto(x, y)
    hi.setheading(90)
    hi.down()
    hi.fd(90)
    hi.circle(-25, 180)
    hi.fd(25)
    hi.circle(-25, 170)
    hi.setheading(315)
    hi.fd(90)

#################

def draw_S(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.setheading(360)
    hi.goto(x, y)
    hi.circle(50, 90)
    hi.down()
    hi.circle(45, 270)
    hi.circle(-45, 270)
############################

def T(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.goto(x, y)
    hi.down()
    hi.setheading(360)
    hi.forward(80)
    hi.bk(40)
    hi.setheading(270)
    hi.forward(100)

#############################
def draw_U(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.goto(-440,200)
    hi.down()
    hi.setheading(270)
    hi.fd(180)
    hi.setheading(300)
    hi.circle(80, 120)
    hi.setheading(90)
    hi.fd(180)

#############################
###############################
############################
###############################

def draw_Y(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.goto(x, y)
    hi.setheading(300)
    hi.down()
    hi.fd(60)
    hi.setheading(60)
    hi.fd(50)
    hi.bk(100)

#############################
#############################

def comma(x = 0, y = 0, color = "white", bg_color = "black"):
    hi.color(color)
    s.bgcolor(bg_color)
    hi.up()
    hi.goto(x, y)
    hi.down()
    hi.setheading(270)
    hi.fd(20)
    hi.circle(-10, 80)

#########################

draw_O()

turtle.done()
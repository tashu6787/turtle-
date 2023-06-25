import turtle
def draw_body1():
    window=turtle.Screen()
    window.bgcolor("White")
    draw_tashu()
    window.exitonclick()

def draw_tashu():
    tashu=turtle.Turtle()
    tashu.shape("turtle")
    tashu.color("red")
    draw_head(tashu)
    draw_body(tashu)
    draw_hand(tashu)
    draw_leg1(tashu)
    draw_leg2(tashu)

def draw_head(tashu):
    tashu.circle(60)
    tashu.speed(3)
    tashu.right(60)

def draw_body(tashu):
    num=0
    while num<3:
        tashu.forward(150)
        tashu.right(120)
        tashu.speed(1)
        num=num+1

def draw_hand(tashu):
    tashu.forward(60)
    tashu.left(60)
    tashu.forward(60)
    tashu.backward(60)
    tashu.right(60)
    tashu.backward(60)

    tashu.right(60)

    tashu.forward(60)
    tashu.right(60)
    tashu.forward(60)

    tashu.backward(60)
    tashu.left(60)
    tashu.forward(90)

def draw_leg1(tashu):
    tashu.left(120)
    tashu.forward(40)
    tashu.right(120)
    tashu.forward(120)
    draw_foot1(tashu)

def draw_leg2(tashu):
    tashu.right(180)
    tashu.forward(120)
    tashu.right(60)
    tashu.forward(70)
    tashu.right(60)
    tashu.forward(120)
    draw_foot2(tashu)

def draw_foot1(tashu):
    tashu.color("blue")
    num=0
    while num<4:
        tashu.forward(20)
        tashu.left(90)
        num=num+1

def draw_foot2(tashu):
    tashu.color("blue")
    num=0
    while num<4:
        tashu.forward(20)
        tashu.left(90)
        num=num+1

draw_body1()

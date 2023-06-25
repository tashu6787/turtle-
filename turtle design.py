import turtle
colors=["red","blue","green","yellow","orange","pink"]
a=turtle.Turtle( )
turtle.bgcolor("black")
for i in range(360):
    a.pencolor(colors[i%6])
    a.width(i/100+1)
    a.forward(i)
    a.left(59)

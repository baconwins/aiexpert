import turtle
turtle.Screen().setup(600,600)
turtle.Screen().bgcolor("green")
pen= turtle.Turtle()
pen.pendown()
size= 10
for side in range(1,101):
    pen.forward(size)
    size=size+10
    pen.right(90)
turtle.done()
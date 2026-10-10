import turtle
turtle.Screen().setup(600,600)
turtle.Screen().bgcolor("green")
pen= turtle.Turtle()
pen.pendown()
size= 10
for side in range(1,4):
    pen.forward(100)

    pen.right(120)
turtle.done()
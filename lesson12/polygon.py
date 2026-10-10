import turtle
turtle.Screen().setup(600,600)
turtle.Screen().bgcolor("green")

pen= turtle.Turtle()
pen.pendown()
for side in range(1,5):
    pen.forward(100)
    pen.right(90)
turtle.done()
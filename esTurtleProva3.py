import turtle

a = turtle.Turtle()

a.speed(0)

a.pencolor("orange")
a.begin_fill()
a.fillcolor("yellow")

for i in range (75):
    a.forward(200)
    a.left(145)
    a.forward(200)

a.end_fill()
a.begin_fill()
a.fillcolor("red")

for i in range (360):
    a.forward(1.1)
    a.left(1)

a.end_fill()

turtle.done()
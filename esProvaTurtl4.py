import turtle

finestra = turtle.Screen()
alice = turtle.Turtle()
bob = turtle.Turtle()
bob.penup()
bob.setposition(-50, 50)
bob.pendown()

alice.forward(100)
alice.right(60)
alice.forward(100)
alice.right(60)

bob.right(90)
bob.backward(80)
bob.left(90)
bob.backward(80)

turtle.done()
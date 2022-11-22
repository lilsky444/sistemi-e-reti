import turtle, random

SPEED = 50000
MS = 10000
MOV = 5

def movimento(robot):
    robot.speed(SPEED)

    for _ in range(MS):
        ran= random.randint(1, 4)
        angolo = 90*ran
        robot.right(angolo)
        robot.forward(MOV)

def main():
    finestra = turtle.Screen()

    robot = turtle.Turtle()
    movimento(robot)

    turtle.done()

if __name__ =="__main__": #"_" = Dunder
    main()
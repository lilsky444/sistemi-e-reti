import turtle
import math

def quadrato(tartarugaQuad):
    for i in range(4):
        tartarugaQuad.forward(100)
        tartarugaQuad.right(90)


def rettangolo(tartarugaRett):
    for i in range(2):
        tartarugaRett.forward(100)
        tartarugaRett.right(90)
        tartarugaRett.forward(50)
        tartarugaRett.right(90)

    
def triangolo(tartarugaTriangolo):
    for i in range(3):
        tartarugaTriangolo.forward(110)
        tartarugaTriangolo.right(120)

def pentagono(tartarugaPentagono):
    for i in range(5):
        tartarugaPentagono.forward(80)
        tartarugaPentagono.right(72)

def esagono(tartarugaEsagono):
    for i in range(6):
        tartarugaEsagono.forward(60)
        tartarugaEsagono.right(60)

def ottagono(tartarugaOttagono):
    for i in range(8):
        tartarugaOttagono.forward(40)
        tartarugaOttagono.right(45)

def decagono(tartarugaDecagono):
    for i in range(10):
        tartarugaDecagono.forward(40)
        tartarugaDecagono.right(36)

def dodecagono(tartarugaDodecagono):
    for _ in range(12):
        tartarugaDodecagono.forward(40)
        tartarugaDodecagono.right(30)

def romboide(tartarugaRomboide):
    for _ in range(2):
        tartarugaRomboide.forward(100)
        tartarugaRomboide.right(120)
        tartarugaRomboide.forward(50)
        tartarugaRomboide.right(60)

def poligono(posx, posy, nLati, colore, curs):
    curs.color("black")
    curs.begin_fill()
    curs.penup()
    curs.setposition(posx, posy)
    curs.pendown()
    angolo = 360/nLati
    lato = 2*40*math.sin(angolo*3.14/180)

    for _ in range(nLati):
        curs.right(angolo)
        curs.forward(lato)

    curs.color(colore)
    curs.end_fill()

def main():
    finestra = turtle.Screen()

    tartarugaQuad = turtle.Turtle()
    tartarugaQuad.penup()
    tartarugaQuad.setposition(-450, 300)
    tartarugaQuad.pendown()

    tartarugaRett = turtle.Turtle()
    tartarugaRett.penup()
    tartarugaRett.setposition(-300, 300)
    tartarugaRett.pendown()

    tartarugaTriangolo = turtle.Turtle()
    tartarugaTriangolo.penup()
    tartarugaTriangolo.setposition(-150, 300)
    tartarugaTriangolo.pendown()

    tartarugaPentagono = turtle.Turtle()
    tartarugaPentagono.penup()
    tartarugaPentagono.setposition(0, 300)
    tartarugaPentagono.pendown()

    tartarugaEsagono = turtle.Turtle()
    tartarugaEsagono.penup()
    tartarugaEsagono.setposition(150, 300)
    tartarugaEsagono.pendown()

    tartarugaOttagono = turtle.Turtle()
    tartarugaOttagono.penup()
    tartarugaOttagono.setposition(-350, 150)
    tartarugaOttagono.pendown()

    tartarugaDecagono = turtle.Turtle()
    tartarugaDecagono.penup()
    tartarugaDecagono.setposition(-200, 150)
    tartarugaDecagono.pendown()

    tartarugaDodecagono = turtle.Turtle()
    tartarugaDodecagono.penup()
    tartarugaDodecagono.setposition(-50, 150)
    tartarugaDodecagono.pendown()

    tartarugaRomboide = turtle.Turtle()
    tartarugaRomboide.penup()
    tartarugaRomboide.setposition(100, 150)
    tartarugaRomboide.pendown()

    quadrato(tartarugaQuad)
    rettangolo(tartarugaRett)
    triangolo(tartarugaTriangolo)
    pentagono(tartarugaPentagono)
    esagono(tartarugaEsagono)
    ottagono(tartarugaOttagono)
    decagono(tartarugaDecagono)
    dodecagono(tartarugaDodecagono)
    romboide(tartarugaRomboide)

    poligono(30, 30, 5, tartarugaRomboide, "red")

    turtle.done()

if __name__ =="__main__": #"_" = Dunder
    main()
#TurtleGraphics.py
#Name: Emma Zechmann
#Date: 2/15/2026
#Assignment: turtle applications 

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def drawPolygon(Diddy, sides):
    for s in range(sides):
        Diddy.forward(25)
        Diddy.right(360/sides)

def fillCorner(fart, corner):
    drawSquare(fart, 50)
    if corner ==(1):
        fart.begin_fill()
        drawSquare(fart,25)
        fart.end_fill()
        fart.penup()
        fart.goto(0,0)
        fart.pendown()
    elif corner == (2):
        fart.forward(25)
        fart.begin_fill()
        drawSquare(fart,25)
        fart.end_fill()
        fart.penup()
        fart.goto(0,0)
        fart.pendown()
    if corner ==(4):
        fart.forward(50)
        fart.right(90)
        fart.forward(25)
        fart.begin_fill()
        drawSquare(fart,25)
        fart.end_fill()
        fart.penup()
        fart.goto(0,0)
        fart.pendown()
    if corner ==(3):
        fart.forward(25)
        fart.right(90)
        fart.forward(25)
        fart.begin_fill()
        drawSquare(fart,25)
        fart.end_fill()
        fart.penup()
        fart.goto(0,0)
        fart.pendown()
        
def squaresInSquares(chickenNugget, number):
    size=50
    for i in range(number):
        
        drawSquare(chickenNugget, size)
        chickenNugget.penup()
        chickenNugget.backward(50)
        chickenNugget.left(90)
        chickenNugget.forward(50)
        chickenNugget.right(90)
        chickenNugget.pendown()
        
        size = size + 100
        
def main():
    myTurtle = turtle.Turtle()
    drawPolygon(myTurtle, 5) #draws a pentagon
    drawPolygon(myTurtle, 8) #draws an octogon

    fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()

import turtle
def drawSquare(sz,alex):
    for i in range(4):
        alex.forward(sz)
        alex.left(90)
        sz -= 5
adnan = turtle.Screen()


alex=turtle.Turtle()
alex.color("red")


sz= 200

for i in range(9):
    drawSquare(sz,alex)
    sz -= 25

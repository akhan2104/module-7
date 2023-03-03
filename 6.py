import turtle
def drawSquare(sz,alex):
    n = 5
    for i in range(4):
        alex.forward(sz)
        alex.left(360/n)
        alex.forward(sz)
        alex.left(50)
        
        sz -= 5
adnan = turtle.Screen()


alex=turtle.Turtle()
alex.color("pink")


sz= 200

for i in range(7):
    drawSquare(sz,alex)
    sz -= 25

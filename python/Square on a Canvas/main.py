import turtle

turtle.Screen().bgcolor("Aqua")

sc = turtle.Screen()
sc.setup(400,300)

turtle.title("Welome to Turtle Window")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1

turtle.done()
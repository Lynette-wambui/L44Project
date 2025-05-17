import turtle

turtle.Screen().bgcolor("Pink")
board = turtle.Turtle( )


# equilateral triangle
board.forward(100) # draw base

board.left(120)
board.forward(120)

board.left(120)
board.forward(120)

board.penup()
board.right(120)
board.forward(0)
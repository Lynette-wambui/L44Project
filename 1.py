import turtle
turtle.Screen().bgcolor("Red")
board = turtle.Turtle( )
num_sides = 6
side_length = 120
angle = 360 / num_sides

# Draw the hexagon
for i in range(6):
    board.forward(120)
    board.left(angle)
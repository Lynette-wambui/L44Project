import turtle

# creating canvas
turtle.Screen().bgcolor("Purple")

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# creating a rectangle
width = 200
height = 150

for i in range(4):
    board.forward(width)
    board.left(90) #Turn 90 degrees left
    board.forward(height)
    board.left(90) #Turn 90 degrees left

    i = i+1
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




import turtle
board = turtle.Turtle( )
num_sides = 6
side_length = 120
angle = 360 / num_sides

# Draw the hexagon
for i in range(6):
    board.forward(120)
    board.left(angle)







import turtle
t = turtle.Turtle()
s = turtle.Screen()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow' ]
s.bgcolor('black')
t.speed('fastest')
t.hideturtle()
while True:
    for x in range(200):
        t.pencolor(colors[x%len(colors)])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(59)
        t.right(239)
        for x in range(200, 0, -1):
            t.pencolor('black')
            t.width(x/100 + 7)
            t.forward(x)
            t.right(59)
import turtle
import random

# Function to generate a random color
def random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

# Function to draw a square with a random color
def draw_square(size):
    turtle.color(random_color())
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

# Function to draw a cool design
def draw_cool_design():
    turtle.speed(2)

    for _ in range(36):
        draw_square(100)
        turtle.right(10)

    turtle.hideturtle()
    turtle.done()

# Call the function to draw the cool design
draw_cool_design()

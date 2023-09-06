import turtle

# Initialize the turtle
star = turtle.Turtle()

# Window title
turtle.title("Star Drawing")

# Set turtle attributes
star.speed(3)  # Fastest speed
star.width(2)  # Set width

for i in range(5):
    star.forward(100)  # Length of the star arm
    star.right(144)  # Turn right

# Close the window on click
turtle.done()

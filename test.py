import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Background color

# Create a turtle
dharani = turtle.Turtle()
dharani.pensize(3)
dharani.color("darkblue")

# Draw a square
for _ in range(4):
    dharani.forward(100)
    dharani.right(90)

# Keep the window open until clicked
screen.exitonclick()

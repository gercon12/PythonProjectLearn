import turtle, colorsys

# Set background color
turtle.bgcolor("black")

# Create turtle object
t = turtle.Turtle()
t.speed(0)  # maximum speed

# Set color mode to 255 (RGB)
turtle.colormode(255)

# Number of circles
n = 36
hue_step = 1 / n
hue = 0

# Draw the swirl
for i in range(360):
    # Convert HSV color to RGB
    col = colorsys.hsv_to_rgb(hue, 1, 1)
    r, g, b = [int(x * 255) for x in col]

    # Set pen color
    t.pencolor(r, g, b)

    # Draw circle
    t.circle(i, 60)
    t.left(10)

    # Increment hue
    hue += hue_step
    if hue >= 1:
        hue = 0

turtle.done()

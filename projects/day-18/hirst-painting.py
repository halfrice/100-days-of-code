import random
import turtle as t
import colorgram


# Move turtle window to front of screen
root = t.getscreen()._root
root.attributes('-topmost', True)

# Window dimensions and options
t.setup(640, 480, None, None)
screen = t.Screen()
screen.colormode(255)
screen.bgcolor('#000000')  # I think it looks cooler with a black background

# Set standard units
gridunits = 10
dotsize = 20
width = screen.window_width()
height = screen.window_height()
xunit = width / gridunits
yunit = height / gridunits

# Set turtle starting position
xstart = -(width - xunit) / 2
ystart = -(height - yunit) / 2

# Turtle options
t.hideturtle()
t.speed(0)
t.penup()
t.goto(xstart, ystart)


# Get a list of colors from an image
def get_colors(pic, n):
    colors_list = []
    colors_from_pic = colorgram.extract(pic, n)
    for c in colors_from_pic:
        r = c.rgb.r
        g = c.rgb.g
        b = c.rgb.b
        colors_list.append((r, g, b))
    return colors_list


# This colors list was obtained by using the function above
# You only need to run this once, then copy and hardcorde colors
# colors = get_colors(pic=('path to pic here'), n=('num of colors here'))

colors = [
    (208, 128, 92),
    (45, 109, 149),
    (26, 183, 155),
    (246, 92, 78),
    (105, 174, 127),
    (190, 97, 106),
    (133, 97, 122),
    (2, 164, 170),
    (78, 139, 136),
    (141, 102, 84),
    (129, 129, 124),
    (0, 111, 117),
    (0, 120, 116),
]

xheading = 0

# Create a grid of dots
for y in range(gridunits):
    t.setheading(90)

    # Skip moving up before laying down dots on the first row only
    if y != 0:
        t.forward(yunit)

    # Use an S or snake pattern to fill each row (back and forth)
    if y % 2 == 0:
        xheading = 0
    else:
        xheading = 180

    for x in range(gridunits):
        t.setheading(xheading)
        t.dot(dotsize, random.choice(colors))

        # Skip moving forward on the last dot of the row
        if x != gridunits - 1:
            t.forward(xunit)

screen.exitonclick()

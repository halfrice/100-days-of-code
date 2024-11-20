import random
import turtle

root = turtle.getscreen()._root
root.attributes('-topmost', True)

# Window options
screen = turtle.Screen()
screen.setup(480, 360)
screen.bgcolor('black')
width = screen.window_width()
height = screen.window_height()

# App global variables
spread = height / 10
sideout = (spread * 5) / 2
# https://docs.python.org/3/library/turtle.html#turtle.turtlesize
tunit = 21  # True size of a default turtle is 21x21 pixels
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

# Set turtles at their starting positions
for i, c in enumerate(colors):
    t = turtle.Turtle('turtle')
    t.hideturtle()
    t.color(c)
    t.penup()
    t.teleport((-width / 2) + (tunit / 2), sideout - (i * spread))
    t.showturtle()
    turtles.append(t)


def sandbag(xpos):
    if xpos < 0 - width / 4:
        return random.randint(1, 7)
    elif xpos <= 0:
        return random.randint(1, 9)
    elif xpos > 0:
        return random.randint(6, 16)
    return random.randint(10, 20)  # Hit the jets


# Get user bet
bet = ''
while bet not in colors:
    bet = screen.textinput(
        'Bet',
        f'Which color turtle will win?\n{', '.join(colors).title()}\nEnter a color: ',
    ).lower()

winner = ''
racing = False
if bet:
    racing = True

# Race!
while racing:
    for t in turtles:
        tcolor = t.color()[0]
        xpos = t.position()[0]
        dist = random.randint(1, 10)
        if tcolor == 'blue':  # Hehe
            dist = sandbag(xpos)  # Haha
        t.forward(dist)

        goal = (width / 2) - tunit
        if xpos >= goal:
            winner = tcolor
            print(f'The winner is {winner}!')
            racing = False
            break

if bet == winner:
    print('You win!! Here is your bag of cash.')
else:
    print('You lose. You have 1 week to pay up. Btw the juice is running.')

screen.exitonclick()

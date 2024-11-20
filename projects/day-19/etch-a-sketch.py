from turtle import Turtle, Screen


t = Turtle()
s = Screen()


# BUG: Research more about how turtle processes graphical updates.
# Press and hold keys introduced some very weird graphics glitches without the tracer
# and update calls. Holding a key caused some batch processesing that would then
# 'deprocess' on key release. Strange...

# Turns off automatic window / graphics updates
s.tracer(0)


def move_forwards():
    t.forward(10)
    # TODO: These update calls are too repetitive. Find a simpler way.
    s.update()


def move_backwards():
    t.backward(10)
    s.update()


def turn_left():
    t.left(10)
    s.update()


def turn_right():
    t.right(10)
    s.update()


def clear():
    s.resetscreen()
    s.update()


# Listener for keypresses
s.listen()

# Keybinds
s.onkey(move_forwards, 'w')
s.onkey(move_backwards, 's')
s.onkey(turn_left, 'a')
s.onkey(turn_right, 'd')
s.onkey(clear, 'c')

s.exitonclick()

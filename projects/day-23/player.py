from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
        self.level = 1

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def is_level_up(self):
        if self.ycor() + 10 > FINISH_LINE_Y:
            self.level += 1
            self.goto(STARTING_POSITION)
            return True
        return False

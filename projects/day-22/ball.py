from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.speed = 0.1
        self.bounce_x()

import random
from turtle import Turtle

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.level = 1
        self.create_cars()

    def add_car(self):
        car = Turtle()
        car.shape('square')
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.penup()
        starting_pos = random.randint(-300, 900), random.randint(-200, 280)
        car.goto(starting_pos)
        self.cars.append(car)

    def create_cars(self, n=30):
        for i in range(n):
            self.add_car()

    def move(self, car):
        if car.xcor() < -340:
            reset_pos = random.randint(300, 900), random.randint(-200, 280)
            car.goto(reset_pos)
        else:
            car.goto(
                car.xcor() - self.speed,
                car.ycor(),
            )

    def increase_level(self, player_level):
        self.level = player_level
        self.speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (self.level - 1))

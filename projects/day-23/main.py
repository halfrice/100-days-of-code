import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crosssing')
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')


def is_collision(player, car):
    if player.distance(car) < 25:
        return True
    return False


game_is_on = True
while game_is_on:
    for car in cars.cars:
        if is_collision(player, car):
            scoreboard.game_over()
            game_is_on = False
            break

        cars.move(car)

    if player.is_level_up():
        cars.increase_level(player.level)
        scoreboard.increase_level(player.level)

    time.sleep(0.1)
    screen.update()

screen.exitonclick()

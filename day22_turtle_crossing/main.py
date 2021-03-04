import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.player_move, 'Up')
cars = []
current_score = 1
scoreboard = Scoreboard(current_score)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_spawn = random.randint(1, 6)

    if car_spawn == 1:
        car = CarManager()
        cars.append(car)

    for each_car in cars:
        each_car.car_move(current_score - 1)
        if player.distance(each_car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.player_reset()
        current_score += 1
        scoreboard.update_score(current_score)


screen.exitonclick()

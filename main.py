import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "w")
screen.onkeypress(player.down, "s")
car_manager = CarManager()

level = 1
game_is_on = True
while game_is_on:
    time.sleep(scoreboard.game_delay)
    screen.update()
    car_manager.show_cars(level)
    car_manager.move_cars(level)

    if player.ycor() > 280:
        player.reset_position()
        level = scoreboard.update_level()
        car_manager.increment_level()
        car_manager.show_cars(level)

    # Detect collision with cars
    cars = 10 + 5*level
    for i in range(cars):
        if car_manager.cars[i].distance(player) < 14:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()


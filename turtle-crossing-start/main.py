import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=player.go_up, key="Up")

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    # Create/update scoreboard
    scoreboard.create_scoreboard()

    # Create a new car
    car_manager.create_car()

    # Move all cars
    car_manager.move_cars()

    # Check collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Check whether the turtle has reached finish
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()

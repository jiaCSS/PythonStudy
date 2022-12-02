from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard
from turtle import Turtle, Screen
import time

screen = Screen ()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(player.go_up, "Up")


    
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_on = False
            scoreboard.gave_over()

    if player.is_finish_line() ==True:
        player.start_point()
        scoreboard.increase_level()
        scoreboard.update_points()
        car_manager.level_up()
        


screen.exitonclick()

import time
from turtle import Screen
import player 
from car_manager import CarManager
from scoreboard import Scoreboard


turtle_player = player.Player()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(turtle_player.up , 'w')
screen.onkey(turtle_player.down , 's')


car_manager = CarManager()

score_board = Scoreboard()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.spawn_car()
    car_manager.move_cars()

    for i in car_manager.cars:
        if turtle_player.distance(i) < 25:

            score_board.end_game()
            time.sleep(5)
           # game_is_on = False
    
    if turtle_player.ycor() == player.FINISH_LINE_Y:

        screen.update()
        turtle_player.move_to_startpos()
        car_manager.next_level()
        score_board.update_score()

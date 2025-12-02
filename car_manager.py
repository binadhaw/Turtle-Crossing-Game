from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7


class CarManager():

    def __init__(self):
        self.cars = []
        self.starting_move_distance = STARTING_MOVE_DISTANCE
        

    def spawn_car(self):

        random_chance = random.randint(1,9)

        if random_chance == 1 or random_chance == 4:
            new_car  = Turtle('square')
            new_car.shapesize(stretch_wid= 1 , stretch_len= 2)
            new_car.penup()
            random_y = random.randint(-250 , 250)
            new_car.goto(265 , random_y)
            car_color = random.choice(COLORS)
            new_car.color(car_color)

            self.cars.append(new_car)
    
    def move_cars(self):
        for car in self.cars:
            car.backward(self.starting_move_distance)
    
    def next_level(self):
        self.starting_move_distance += MOVE_INCREMENT 

        
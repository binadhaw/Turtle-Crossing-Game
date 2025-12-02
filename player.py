from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def move_to_startpos(self):
        self.penup()
        self.goto(STARTING_POSITION)

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.tilt(90)
        self.color('black')
        self.move_to_startpos()

        self.move_amount = 10

    
    def up(self):
        self.goto(self.xcor() , self.ycor() + self.move_amount)
        
    def down(self):
        self.goto(self.xcor() , self.ycor() - self.move_amount)

  
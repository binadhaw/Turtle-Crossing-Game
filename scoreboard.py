from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-275, 250)
        self.write(self.score , font=('Arial' , 25 , 'normal'))
    
    def update_score(self):
        
        self.clear()
        self.score +=1
        self.write(self.score , font=('Arial' , 25 , 'normal'))
    
    def end_game(self):

        self.clear()
        self.goto(0,0)
        self.write("Game Over", font=('Arial' , 30 , 'normal'))

    

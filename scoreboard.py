from turtle import Turtle
#Turtle library for graphics.

ALIGNEMT = "center"
FONT = ("courier",14,"normal")

#Create a scoreboard
class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,275)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGNEMT,font = FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align=ALIGNEMT,font = FONT)
        
    
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
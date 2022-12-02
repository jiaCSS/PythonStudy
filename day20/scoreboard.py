from turtle import Turtle
ALINGN = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color ( "white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="Center", font = ("Arial", 24, "normal"))
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align="Center", font = ("Arial", 24, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALINGN, font = FONT)
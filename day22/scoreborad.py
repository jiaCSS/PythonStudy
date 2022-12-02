from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.score = 0
        self.x = x
        self.y = y
        self.write(f"Score: {self.score}", align= "center", font = ("Arail", 20, "normal"))
    
    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align= "center", font = ("Arail", 20, "normal"))
        print("thiis is jai")
        
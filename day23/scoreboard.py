from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self) :
            super().__init__()
            self.level = 1
            self.hideturtle()
            self.color("black")
            self.penup()
            self.goto(0, 250)
            self.score = 0
            self.write(f"level {self.level}", align = "center", font =("Arail", 20, "normal"))
            pass
    
    def gave_over(self):
        
        self.goto(0, 0)
        self.write("gave over", align="center", font = ("Arail", 25, "normal"))
    
    def update_points(self):
        self.score += 1
        self.clear()
        self.write(f"level: {self.level}", align = "center", font =("Arail", 20, "normal"))
    
    def increase_level(self):
        self.level += 1
        
    pass
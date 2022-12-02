from turtle import Turtle
FINISH_LINE = 260
STARTING_POINT = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POINT)
        self.left(90)
    
    def go_up(self):
        y_position = self.ycor() +10
        self.goto(self.xcor(), y_position)
    
    def is_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False
    
    def start_point(self):
        self.goto(STARTING_POINT)

    
    pass
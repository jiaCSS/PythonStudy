from turtle import Turtle, Screen
import random
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

STARTING_POSITIONS  = [(0, 0),  (-20, 0), (-40, 0),]
MOVE_DISTANCE =20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = [ ]
        self.creat_snake()
        self.heading = self.segments[0]
        
    def creat_snake(self):
        for index in STARTING_POSITIONS:
            self.add_segment(index)
            
            
    def add_segment(self, index):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()             
            new_turtle.goto(index)
            self.segments.append(new_turtle)
        

    def extend(self):
        self.add_segment(self.segments[-1].index())
           
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.heading.heading() != DOWN:
            self.heading.setheading(UP)
        
    def down(self):
        if self.heading.heading() != UP:
            self.heading.setheading(DOWN)
        
    def left(self):
        if self.heading.heading() != RIGHT:
            self.heading.setheading(LEFT)
        
    def right(self):
        if self.heading.heading() != LEFT:
            self.heading.setheading(RIGHT)
    
    def hit_wall(self):
        if self.heading.xcor() > 280 or self.heading.xcor() < -280 or self.heading.ycor() > 280 or self.heading.ycor() < -280:
            # print(self.heading.xcor())
            return False
        else:
            return True
        
        
snake = Snake()
food = Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
#    detect collision with food.
    if snake.heading.distance(food) < 15:
       food.refresh()
       snake.extend()
       
       scoreboard.score +=1
       scoreboard.increase_score()
      
       
    if snake.hit_wall() == False:
        game_is_on = False
        scoreboard.game_over()
    
    # if snake.heading.xcor() > 280 or snake.heading.xcor() < -280 or snake.heading.ycor() > 280 or snake.heading.ycor() < -280:
    #     scoreboard.game_over()
           
    # detect collision with tail:
    # if head collides with any segment in the tail:
    # add segment ==snake.heading: because first loop through is the heading, so will stop the game
    # for segment in snake.segments:
    #     if segment == snake.heading:
    #         pass
    #     elif snake.heading.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
# short version it is easy by using slicing

    for segment in snake.segments[1:]:
        if snake.heading.distance(segment)< 10:
            game_is_on = False
            scoreboard.game_over()


        











screen.exitonclick()
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreborad import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle(-300, 0)
r_paddle = Paddle(300, 0)
ball = Ball()
scoreboard_l = Scoreboard(-200, 200)
scoreboard_r = Scoreboard(200, 200)


screen.listen()
screen.onkey(l_paddle.paddle_up, "Up")
screen.onkey(l_paddle.paddle_down, "Down")
screen.onkey(r_paddle.paddle_down, "Left")
screen.onkey(r_paddle.paddle_up, "Right")

game_is_on =True

while game_is_on :
    time.sleep(0.1)
    screen.update()   
    
    ball.move()
    
    if ball.ycor() > 320 or ball.ycor() < -320:
        ball.bounce_y()
        
    if ball.distance(r_paddle)<50 and ball.xcor() >320 or ball.distance(r_paddle)<50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor()>380:
        ball.reset()
        scoreboard_l.update()
        
    if ball.xcor()< -380:
        ball.reset()
        scoreboard_r.update()
        
        
    
        
            

        
           
    # hit the ball
     

 
    










screen.exitonclick()

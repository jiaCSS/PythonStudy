from turtle import Turtle, Screen
import random
import turtle
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet: red, orange, blue, purple, yellow green ", prompt = "which turtle will win the race? enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]

all_turtles = []
for index in range ( 0, 6):
    
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[index])
    # new_turtle.pendown()
    all_turtles.append(new_turtle)
         
is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on : 
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! the {winning_color} turtle is the winner!")
            else: 
                print(f"you've lost! the {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        






screen.exitonclick()
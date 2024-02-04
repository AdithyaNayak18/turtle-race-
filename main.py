from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which Turtle will win the race? Enter a color : ")
colors = ["red", "yellow", "blue", "green", "black"]
y_positions = [-100, -50, 0, 50, 100]
all_turtles = []

for i in range(0, 5):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've Won! {win_color} is the winner!")
            else:
                print(f"You've Lost! {win_color} has won!")
            exit(0)
        rand_distance = random.randint(0, 15)
        turtle.forward(rand_distance)

screen.exitonclick()

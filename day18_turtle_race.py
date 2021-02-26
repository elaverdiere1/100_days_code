from turtle import Turtle, Screen
import random

# setting up the screen and the user guess
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title='Make your bets', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []

# creating the racers
for x in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[x])
    new_turtle.goto(x=-230, y=y_position[x])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

# sets up the running of the race
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                is_race_on = False
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

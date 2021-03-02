from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

# set screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# pull from classes
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

# wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

# paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

# check score right
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

# check score left
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()

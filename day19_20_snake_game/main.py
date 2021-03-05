from turtle import Screen
import time
from food import Food
from score import Score
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.snake_list[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.snake_list[0].xcor() > 280 or snake.snake_list[0].xcor() < -280 or snake.snake_list[0].ycor() > 280 or snake.snake_list[0].ycor() < -280:
        score.reset_score()
        snake.reset()

    for snakes in snake.snake_list[1:]:
        if snake.snake_list[0].distance(snakes) < 10:
            score.reset_score()
            snake.reset()


screen.exitonclick()


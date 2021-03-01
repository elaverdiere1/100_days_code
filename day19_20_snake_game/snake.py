from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()

    def create_snake(self):
        for x in range(3):
            position = (0 - (x * 20), 0)
            self.add_segment(position)


    def move_snake(self):
        for snakes in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[snakes - 1].xcor()
            new_y = self.snake_list[snakes - 1].ycor()
            self.snake_list[snakes].goto(new_x, new_y)
        self.snake_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_list[0].heading() != 270:
            self.snake_list[0].setheading(90)

    def down(self):
        if self.snake_list[0].heading() != 90:
            self.snake_list[0].setheading(270)

    def left(self):
        if self.snake_list[0].heading() != 0:
            self.snake_list[0].setheading(180)

    def right(self):
        if self.snake_list[0].heading() != 180:
            self.snake_list[0].setheading(0)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def add_segment(self, position):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.setposition(position)
        self.snake_list.append(snake)
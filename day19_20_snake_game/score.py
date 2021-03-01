from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f'Score: {self.current_score}', align='center', font=('Ariel', 24, 'normal'))

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=('Ariel', 24, 'normal'))

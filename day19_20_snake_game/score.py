from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'Score: {self.current_score}  High Score: {self.high_score}', align='center', font=('Ariel', 24, 'normal'))

    def increase_score(self):
        self.current_score += 1
        self.update_score()

    def reset_score(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.high_score}")
        self.current_score = 0
        self.update_score()

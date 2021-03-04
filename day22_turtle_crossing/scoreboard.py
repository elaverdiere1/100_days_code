from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.update_score(score)

    def update_score(self, score):
        self.clear()
        self.goto(-200, 260)
        self.write(arg=f'Level: {score}', align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='Game Over', align='center', font=FONT)

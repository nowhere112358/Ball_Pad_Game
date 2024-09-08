from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.rscore = 0
        self.lscore = 0
        self.color('white')
        self.penup()
        self.hideturtle()

    def up_date_score(self):
        self.clear()
        self.goto(200, 170)
        self.write(self.rscore, align='center', font=('courier', 50, 'normal'))
        self.goto(-200, 170)
        self.write(self.lscore, align='center', font=('courier', 50, 'normal'))



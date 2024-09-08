from turtle import Turtle
class Pad (Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.speed('fast')
        self.penup()
        self.goto(xcor, ycor)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 50)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 50)







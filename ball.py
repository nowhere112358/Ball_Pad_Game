from turtle import Turtle
import random

class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.xmove = 10
        self.ymove = 10
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)

    def bounce_wall(self):
        self.ymove = self.ymove * (-1)

    def bounce_pad(self):
        self.xmove = self.xmove * (-1)
        self.speed *= 0.95

    def set_pos_ori(self):
        self.speed = 0.1
        self.goto(0, 0)
        self.bounce_pad()











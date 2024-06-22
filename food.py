from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        x_pos = randint(-280, 280)
        y_pos = randint(-280, 280)
        self.goto(x_pos, y_pos)

    def refresh(self):
        x_pos = randint(-280, 280)
        y_pos = randint(-280, 280)
        self.goto(x_pos, y_pos)

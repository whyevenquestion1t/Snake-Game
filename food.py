from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("slowest")
        self.refresh()

    def refresh(self):
        self.goto(y=random.randint(-270, 270), x=random.randint(-270,270))



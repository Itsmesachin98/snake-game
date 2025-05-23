from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        randon_x = random.randint(-260, 260)
        randon_y = random.randint(-260, 260)
        self.goto(randon_x, randon_y)
        
import time
from turtle import Turtle, Screen

screen = Screen()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_pos = 1
        self.x_pos = 1

    def move(self):
        time.sleep(0.1)
        self.sety(self.ycor() + (self.y_pos * 20))
        self.setx(self.xcor() + self.y_pos * 20)





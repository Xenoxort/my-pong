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
        self.speed = 1

    # Move ball
    def move(self):
        time.sleep(0.01 / self.speed)
        self.sety(self.ycor() + (self.y_pos * 5))
        self.setx(self.xcor() + self.x_pos * 5)

    # Bounce from wall
    def bounce_wall(self):
        self.y_pos *= -1

    # Bounce from paddle and speed up ball
    def bounce_paddle(self):
        self.x_pos *= -1
        self.speed *= 1.5





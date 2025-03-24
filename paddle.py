from turtle import Turtle, Screen

screen = Screen()

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(pos)

    #Keyboard functions
    def up(self):
        if self.ycor() < 260:
            self.sety(self.ycor() + 30)

    def down(self):
        if self.ycor() > -260:
            self.sety(self.ycor() - 30)



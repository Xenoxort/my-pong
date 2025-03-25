from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")

class Score(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(pos)
        self.update_score()


    def update_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()




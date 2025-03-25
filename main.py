import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

# Screen Setup
height = 600
width = 800

screen = Screen()
screen.setup(width=width, height=height)
screen.bgcolor("black")
screen.title("My Pong Game")

screen.tracer(0)
# Middle Line
tim = Turtle()
tim.hideturtle()
tim.color("white")
tim.penup()
tim.goto(0, height/2 - 15)
tim.setheading(270)
tim.pendown()
tim.pensize(3)

while tim.ycor() > -(height/2 - 15):
    tim.forward(20)
    tim.penup()
    tim.forward(10)
    tim.pendown()


# Create Paddles
pos_left_paddle = (-(width/2-50), 0)
pos_right_paddle = ((width/2-50), 0)

left_paddle = Paddle(pos_left_paddle)
right_paddle = Paddle(pos_right_paddle)

# Controlling Paddles
screen.listen()

screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

# Ball
my_ball = Ball()

#Scoreboard
pos_left_score = (-60, (height/2 -60))
pos_right_score = (60, (height/2 - 60))

left_score = Score(pos_left_score)
right_score = Score(pos_right_score)

screen.update()

# Game
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    my_ball.move()

    # Bounce wall
    if my_ball.ycor() > (height/2 - 25) or my_ball.ycor() < -(height/2 - 25):
        my_ball.bounce_wall()

    # Bounce paddle
    if ((width/2-70) < my_ball.xcor() < (width/2-60) and my_ball.distance(right_paddle) < 50) or (-(width/2-60) < my_ball.xcor() < -(width/2-70) and my_ball.distance(left_paddle) < 50):
        my_ball.bounce_paddle()

    #screen.update()

    # Update Score
    if my_ball.xcor() < -width / 2:
        right_score.increase_score()
        my_ball.restart()

    if my_ball.xcor() > width/2:
        left_score.increase_score()
        my_ball.restart()

    screen.update()


screen.exitonclick()
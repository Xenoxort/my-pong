import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball


# Screen Setup
width = 800
height = 600

screen = Screen()
screen.setup(width=width, height=height)
screen.bgcolor("black")
screen.title("My Pong Game")


# Create Paddles
screen.tracer(0)

pos_left = (-(width/2-50), 0)
pos_right = ((width/2-50), 0)

left_paddle = Paddle(pos_left)
right_paddle = Paddle(pos_right)

# Controlling Paddles
screen.listen()

screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

# Ball
my_ball = Ball()

screen.update()

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    my_ball.move()

    # Bounce wall
    if my_ball.ycor() > (height/2 - 25) or my_ball.ycor() < -(height/2 - 25):
        my_ball.bounce_wall()

    # Bounce paddle
    if (330 < my_ball.xcor() < 340 and my_ball.distance(right_paddle) < 50) or (-340 < my_ball.xcor() < -330 and my_ball.distance(left_paddle) < 50):
        my_ball.bounce_paddle()


    screen.update()




screen.exitonclick()
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT_POSITION = (350, 0)
LEFT_POSITION = (-350, 0)

screen = Screen()
screen.setup(800, 600)
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

right_paddle = Paddle(RIGHT_POSITION)
left_paddle = Paddle(LEFT_POSITION)
ball = Ball()
scoreboard = Scoreboard()


screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 400:
        ball.new_ball_position()
        scoreboard.increase_left_score()
    elif ball.xcor() < -400:
        ball.new_ball_position()
        scoreboard.increase_right_score()

    if scoreboard.left_score == 11:
        scoreboard.left_winner()
        game_on = False
    elif scoreboard.right_score == 11:
        scoreboard.right_winner()
        game_on = False

screen.exitonclick()

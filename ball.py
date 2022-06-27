from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.penup()
        self.x_pos = 10
        self.y_pos = 10
        self.moving_speed = 0.1

    def move_ball(self):
        x_coordinates = self.xcor() + self.x_pos
        y_coordinates = self.ycor() + self.y_pos
        self.goto(x_coordinates, y_coordinates)

    def x_bounce(self):
        self.x_pos *= -1
        self.moving_speed *= 0.9

    def y_bounce(self):
        self.y_pos *= -1
        self.moving_speed *= 0.9

    def new_ball_position(self):
        self.goto(0, 0)
        self.x_bounce()


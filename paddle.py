from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(self.position)

    def move_up(self):
        y_pos = self.ycor() + 25
        self.goto(self.xcor(), y_pos)

    def move_down(self):
        y_pos = self.ycor() - 25
        self.goto(self.xcor(), y_pos)

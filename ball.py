from turtle import Turtle, Screen
import random

random_x = random.randint(0, 330)
random_y = random.randint(0, 330)
screen = Screen()
screen.tracer(10)
screen.update()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x = 10
        self.y = 10

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x*=-1

    def reset(self) :
        self.goto(0,0)
        self.bounce_x()

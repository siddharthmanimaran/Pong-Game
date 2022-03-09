from turtle import Turtle,Screen
import random

random_x= random.randint(0, 330)
random_y= random.randint(0, 330)
screen=Screen()
screen.tracer(10)
screen.update()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        # self.goto(random_x,random_y)

    def move(self):
        new_x=self.xcor()+10
        new_y=self.ycor()+10
        self.goto(new_x,new_y)

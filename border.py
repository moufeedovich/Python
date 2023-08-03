from turtle import Turtle

class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.pencolor("black")
        self.goto(-300, -300)
        self.pendown()
        self.forward(600)
        self.setheading(90)
        self.forward(600)
        self.setheading(180)
        self.forward(600)
        self.setheading(270)
        self.forward(600)

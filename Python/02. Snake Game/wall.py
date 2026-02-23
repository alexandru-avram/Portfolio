from turtle import Turtle

class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("white")
        self.pensize(5)
        self.goto(-420, -420)
        self.pendown()
        self.goto(420,-420)
        self.goto(420,420)
        self.goto(-420,420)
        self.goto(-420,-420)
        self.hideturtle()
from turtle import Turtle

class HalfField(Turtle):
# class for the line of the half accrots
     def __init__(self):
        super().__init__()
        down_half = Turtle()
        top_half = Turtle()

        top_half.hideturtle()
        down_half.hideturtle()
        down_half.color("white")
        down_half.shape("square")
        down_half.shapesize(1,0.3)
        down_half.setheading(270)
        down_half.forward(330)

        top_half.color("white")
        top_half.shape("square")
        top_half.shapesize(1,0.3)
        top_half.setheading(90)
        top_half.forward(330)
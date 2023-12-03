from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        #self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.speed("fastest")

    def getUp(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def getDown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)    

    def touchTopFrame(self):
        if(self.ycor() >= 280):
            self.getDown()
    
    def touchDownFrame(self):
        if(self.ycor() <= -280):
            self.getUp() 
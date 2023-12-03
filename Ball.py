from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("purple")
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 7

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move = self.y_move * -1

    def bounce_x(self):
         self.x_move =  self.x_move * -1

    def afterRightLimit(self):
        if self.xcor() > 400:
            self.home()
            self.bounce_x()
            self.bounce_y()
            return True
        return False
    
    def afterLeftLimit(self):
        if self.xcor() < -400:
            self.home()
            self.bounce_x()
            self.bounce_y()
            return True
        return False

    



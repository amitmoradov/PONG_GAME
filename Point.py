from turtle import Turtle


class Point(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()

    def add_point(self):
        pass
        self.score = self.score + 1
        return self.score
    
    def writeScorePage(self):
        pass
        self.clear()
        self.write(f"POINT: {self.score}",align="center",font=("Arial",18,"normal"))
    
    def current_point(self):
        return self.score
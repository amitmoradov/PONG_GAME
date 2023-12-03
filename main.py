from turtle import Turtle,Screen
import turtle
from Paddle import Paddle
from Ball import Ball
import time
from Point import Point
from HalfField import HalfField


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")

image = "./pong_image.gif"
screen.addshape(image)
turtle.shape(image)

screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle()
right_paddle = Paddle()
right_point = Point() 
left_point = Point()
ball = Ball()
#half_field = HalfField()

right_paddle.color("blue")
left_paddle.color("red")
#user1 = screen.textinput("choice your paddle (left/right)")
screen.listen()


screen.onkey(right_paddle.getUp,"Up")
screen.onkey(right_paddle.getDown,"Down")

screen.onkey(left_paddle.getUp,"w")
screen.onkey(left_paddle.getDown,"x")

right_paddle.goto(375,0)
left_paddle.goto(-383,0)

right_point.goto(100,270)
left_point.goto(-100,270)
left_point.write(f"POINT: {right_point.score}",align="center",font=("Arial",18,"normal"))
right_point.write(f"POINT: {left_point.score}",align="center",font=("Arial",18,"normal"))


game_over = False
while game_over != True:
    time.sleep(0.1) # couse to game run morer slowly
    screen.update()
    ball.move()
    if(ball.ycor()>= 290 or ball.ycor()<= -290): # Checks if the ball has reached the boundaries
    # so that it jumps in the other direction
        ball.bounce_y()

    if(right_point.current_point() == 5):
        print(f"THE RIGHT PANDDLE IS WINNING THE GAME")
        game_over = True

    if(left_point.current_point() == 5):
        print(f"THE LEFT PANDDLE IS WINNING THE GAME")
        game_over = True

    if(ball.afterRightLimit()):
        left_point.add_point()
        left_point.writeScorePage()
        

    if(ball.afterLeftLimit()):
        right_point.add_point()
        right_point.writeScorePage()


    if(ball.distance(right_paddle) < 40 and ball.xcor() > 355):
        ball.bounce_x()

    if(ball.distance(left_paddle) < 40 and ball.xcor() < -353):
        ball.bounce_x()   


    left_paddle.touchTopFrame()
    left_paddle.touchDownFrame()

    right_paddle.touchDownFrame()
    right_paddle.touchTopFrame()




screen.exitonclick()
# day19 - Event Listeners & Higher Order Functions

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_right():
    tim.forward(10)

screen.listen()
screen.onkey(key='d', fun=move_right)
screen.exitonclick()

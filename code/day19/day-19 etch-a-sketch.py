# day19 Project - Etch-a-sketch

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_right():
    new_heading = tim.heading() - 20
    tim.setheading(new_heading)
    tim.forward(30)


def move_left():
    new_heading = tim.heading() + 20
    tim.setheading(new_heading)
    tim.forward(30)


def move_back():
    tim.backward(30)


def move_forward():
    tim.forward(30)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
# screen.onkey(key='d', fun=move_right)
# screen.onkey(key='a', fun=move_left)
# screen.onkey(key='w', fun=move_forward)
# screen.onkey(key='s', fun=move_back)

screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(move_forward, "w")
screen.onkey(move_back, "s")
screen.onkey(clear, "c")


screen.exitonclick()

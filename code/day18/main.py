# day 18 - Turtle Graphics
import turtle
from turtle import Turtle, Screen
import random

# from turtle import *       - imports everything from turtle

timmy = Turtle()
timmy.shape("arrow")

for a in range(4):
    turtle.forward(100)
    turtle.left(90)

for a in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen"]
timmy.speed("fastest")
timmy.pensize(15)
directions = [0, 90, 180, 270]

for _ in range(200):
    timmy.color(random.choice(colours))
    timmy.forward(50)
    timmy.setheading(random.choice(directions))


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        # timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()

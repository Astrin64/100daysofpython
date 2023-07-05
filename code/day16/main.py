# day16 - OOP - Classes and Objects
import turtle
from turtle import Screen
from prettytable import PrettyTable

# Attributes are variables attached to an object (what it has)
# Methods are functions attached to an object (what it does)

# Classes are blueprints to create objects; obj = ClassName; PascalCase
# car = car.CarBluePrint()

# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("cyan1")
# timmy.forward(100)

# Or: from turtle import Turtle
# timmy = Turtle()

# my_screen = Screen()
# print(my_screen.canvheight)  # attribute
# my_screen.exitonclick()  # method

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)

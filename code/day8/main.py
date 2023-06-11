# day8 - Functions with input

def greet():
    print("Good morning")
    print("Good afternoon")
    print("Good evening")


# def function (parameter)
#       #Pass an argument into the parameter

def greet_with_name(name):
    print("Hello " + name)
    print("Good morning")


greet_with_name(input("What is your name? "))


# Functions with more than 1 parameter
def greet_with(name, location):
    print("Hey there " + name)
    print("How is the weather in " + location)


# This is a keyword argument below; name = name, location = location, make sure the arg position is correct
#eg: greet_with(location = "St. Cloud", name = "Ameen")

greet_with(input("What is your name? \n"), input("Where do you live? \n"))

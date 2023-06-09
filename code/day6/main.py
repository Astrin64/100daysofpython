#day6 - Functions & Karel

def my_function():
    print("Hello")
    print("Bye")

my_function()

#Karel - reeborg.ca - Hurdle 1
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# def hurdle():
#     move()
#     jump()

# hurdle()
# hurdle()
# hurdle()
# hurdle()
# hurdle()
# hurdle()
#OR
# for step in range(6):
#     hurdle()
#OR
#use a While loops
# num_of_hurdles = 6
# while num_of_hurdles > 0:
#     jump()
#     num_of_hurdles -=1


#Karel - reeborg.ca - Hurdle 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
#day4 randomisation

import random

# random_integer = random.randint(1, 10)
# print(random_integer)
#
# random_float = random.random() + random_integer
# print(random_float)

#Ctrl + / to comment multiple lines

#Lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
print(states_of_america[0])
print(states_of_america[-1])

states_of_america[1] = "Pencilvania"
print(states_of_america)

states_of_america.append("New State")
print(states_of_america)

states_of_america.extend(["New State1", "New State2"])
print(states_of_america)


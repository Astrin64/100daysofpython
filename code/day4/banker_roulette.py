#Day4 - Banker Roulette
import random

names_string = input("Give me everyone's names, separated by a comma. \n")
names = names_string.split(", ")

num_names = len(names)
buyer = random.randint(0, num_names - 1)
person_who_pays = names[buyer]
print(f"The person who will pay today is {person_who_pays}!")

#OR this method

person_who_pays = random.choice(names)
print(f"The person who will pay today is {person_who_pays}!")

#Jane, Joe, Jimmy, Jack

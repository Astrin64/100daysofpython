#day12 - Number guessing game
import random
import sys

Hard_Attempts = 5
Easy_Attempts = 10

def game():
    answer = random.randint(1, 100)
    print(answer)

    print("Welcome to the Number Guessing Game \nI'm thinking of a number from 1 to 100")
    difficulty = input("Easy or Hard: ")
    if difficulty == "easy":
        attempts = 10
    else: attempts = 5

    def guess():
        guess = int(input("Make a guess: "))
        if guess == answer:
            print("You got it right! \nYou win!")
            sys.exit()
        elif guess > answer:
            print("Too high")
        elif guess < answer:
            print("Too low")

    while attempts != 0:
        print(f"You have {attempts} attempts left")
        guess()
        attempts -= 1


    def retry():
        retry = input("\nWant to try again? \nType 'y' or 'n': ").lower()
        if retry == 'y':
            game()
        else:
            sys.exit()

    if attempts == 0:
        retry()

game()

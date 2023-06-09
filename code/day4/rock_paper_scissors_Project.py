#Day4 - Rock Paper Scissors project
import random

user_choice = int(input("What move will you make? Type 0 for rock, 1 for Paper or 2 for scissors. \n"))
cpu_move = random.randint(0, 2)
print(f"The computer chose: {cpu_move}")

if user_choice >= 3 or user_choice < 0:
    print("That's an invalid number")
elif user_choice == 0 and cpu_move == 2:
    print("You win!")
elif cpu_move== 0 and cpu_move == 2:
    print("You lose!")
elif cpu_move > user_choice:
    print("You lose")
elif user_choice > cpu_move:
    print("You win")
elif cpu_move == user_choice:
    print("It's a draw")


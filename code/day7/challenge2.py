#day 7 - challenge2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_len = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
display = []
for letter in chosen_word:
    display.append("_")
print(display)
guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


for position in range(word_len):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)


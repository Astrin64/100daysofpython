# Day 13 - Debugging

# Describe Problem
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

#You have to change range to 21 bc range(1,21) doesn't have 20 in range
my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

#This error is bc of ListError, it should be (0, 5) instead

# # Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
#This bug is bc there is no >= or <= for 1994 so 1994 doesn't print anything


# # Fix the Errors
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")
#This has an indentation error, missing the f for fStrings and age is str, so this is a TypeError

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
#word_per_page has comparison operator, multiplies with 0

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
#This has a indentationError on line 49, it's outside the loop and so only updates b_list once

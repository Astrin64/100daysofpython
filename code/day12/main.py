# day 12 - Scope and Namespace

enemies = 1

def increase_enemies():
    #global enemies -> this function calls the one listed above and lets you modify it
    enemies = 2 #<- this is a diff variable than the one listed above
    print(f"enemies inside function: {enemies}")
    # outputs 2


increase_enemies()
print(f"enemies outside function: {enemies}")
# outputs 1

# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    # you can only use potion_strength locally inside the drink potion function


# Global Scope
player_health = 10


def drink_potion():
    potion_strength = 2
    print(player_health)

# You can print player health outside since it's a global variable
#No Block scope in Python like in Java or C++ like if/else, these are global scope

#Global Constants
PI = 3.14159 #conts variables are all named in uppercase
URL = "www..."





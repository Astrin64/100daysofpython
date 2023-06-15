#day9 - Dictionaries

programming_dictionary = {
    "Bug": "An error in a program prevents it from running as expected",
    "Function": "A piece of code that you can reuse easily",
}

print(programming_dictionary["Bug"])
#If you misspell when calling from dictionary, it gives a KeyError

#adding new items to the dictionary
programming_dictionary["Loop"] = "The action of repeating a set of instructions"

#Create an empty dictionary
programming_dictionary = {}

#edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer."

#Loop through a dictionary
for item in programming_dictionary:
    print(item)
    #prints out Bug, Function andLoop

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    #prints out both the name and values
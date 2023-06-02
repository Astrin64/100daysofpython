#day5 - loops

#For Loops
fruits = ["Apple","Pear", "Peach"]
for fruit in fruits:
    print(fruit)
#    print(fruit + " Pie")


#For loop with range
#(1,10) = 1 - 9, last number excluding
#steps (1, 11, 3) = 1, 4, 7, 10

total = 0
for number in range(1, 101):
    total += number
print(total)

#add all even numbers
even_numbers = 0
for number in range(0, 101, 2):
    even_numbers += number
print(even_numbers)
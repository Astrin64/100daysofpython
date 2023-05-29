#Tip Calculator - Day2 Final

print("Welcome to the tip calculator")
bill = float(input("How much was the total bill? \n"))
numOfPeople = int(input("How many people are joining you? \n"))
tip = int(input("What percentage tip would you like to give? \n"))

tipPercent = tip / 100
billWithTip = round(bill + (tipPercent * bill), 2)

billPerPerson = round(billWithTip / int(numOfPeople), 2)
print(f"The new total is ${billWithTip} and each person pays ${billPerPerson}")
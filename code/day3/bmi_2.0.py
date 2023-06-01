# BMI 2.0 calculator - Day 3

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2, 2)
print(bmi)

if bmi < 18.5:
    print("Your BMI is underweight")
elif bmi < 25:
    print("Your BMI is normal")
elif bmi < 30:
    print("Your BMI is overweight")
elif bmi < 35:
    print("Your BMI is obese")

# (2) BMI calculator.

print("enter your weight (Kg)")
weight = float(input())

print("enter your height (m)")
height = float(input())

bmi = weight / (height ** 2)
print(f"your BMI is : {bmi:.2f}")
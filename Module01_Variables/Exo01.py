
# module 1 : variables.

# (1) farenit.

print("enter a temperature (in Celsius).")
celsius = input()
celsius_int = None

try:
    celsius_int = float(celsius)
except:
    print("error : input is not a number")

if celsius_int != None:
    fahrenheit = celsius_int * (9 / 5) + 32
    print(f"in fahrenheit : {fahrenheit:.2f}")

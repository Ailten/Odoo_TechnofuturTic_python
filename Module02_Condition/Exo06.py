import random

# guess the price.

price_to_guess = int(random.random() * 100)

print("enter a number to guess")

while True:
    
    num_try = int(input())

    if num_try == price_to_guess:
        break
    
    if num_try > price_to_guess:
        print("to big")
    else:
        print("to low")

print("congrats !")
import math

# piramide star.

print("enter a number")
num = int(input())

# security to take even only.
if num % 2 == 0:
    num_even = num - 1
    print(f"{num} is an odd number, so it was floor to {num_even}.")
    num = num_even

for i in range( num // 2, -1, -1):
    print(
        ' ' * i, 
        '# ' * math.ceil((num - i * 2) / 2)
    )
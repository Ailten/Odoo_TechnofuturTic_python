
# square hole.

print("enter a number")
length = int(input())

for i in range(0, length, 1):
    if i == 0 or i == length - 1:
        print('#' * length)
    else:
        print(
            '#',
            ' ' * (length - 4),  # minus 2.
            '#'
        )
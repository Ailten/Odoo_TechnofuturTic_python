
# piramide star.

# FIXME : re do with space into (fill with damier).

print("enter a number")
num = int(input())

for i in range( num // 2, -1, -1):
    print(
        ' ' * i, 
        '#' * (num - i * 2),
        ' ' * i
    )
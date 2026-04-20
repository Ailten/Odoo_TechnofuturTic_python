
# fizz buzz.

print("enter a number.")
max_value = int(input())

for i in range(1, max_value + 1, 1):

    if i % 3 == 0 and i % 5 == 0:
        print('fizz-buzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(str(i))

# even or odd.

print("enter a number")
input_num = int(input())

is_odd = input_num % 2 == 0
is_odd_str = "even" if is_odd else "odd"

print(
    f"your number is {is_odd_str}"
)
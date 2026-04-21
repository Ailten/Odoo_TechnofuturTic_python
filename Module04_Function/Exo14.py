
def my_func(*n: str) -> int:
    return len(n)

a = my_func
print(a('a', 'b'))


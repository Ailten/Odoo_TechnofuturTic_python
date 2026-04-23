import cProfile

# bubule sort.
# big O search. (split in half)
# quit sort. (split in half)
# merge sort. (split in half)

def search(n :int, list_int: list):
    if len(list_int) == 0:
        return False
    half_index = len(list_int) // 2
    value_half = list_int[half_index]
    if n == value_half:
        return True
    if n < value_half:
        return search(n, list_int[:half_index - 1])
    return search(n, list_int[half_index + 1:])

# non-recursive vertion to avoir creation sub list.
def search_non_recurcive(n: int, list_int: list):
    min_i = 0
    max_i = len(list_int)
    while max_i - min_i != 0:
        mid_i = min_i + ((max_i - min_i) // 2)
        mid_value = list_int[mid_i]
        if mid_value == n:
            return True
        if n < mid_value:
            max_i = mid_value
        min_i = mid_value
    return False




l = [0,1,2,5,3,9,8,4,7,6]
cProfile.run('search(42, '+str(l)+')')
cProfile.run('search_non_recurcive(42, '+str(l)+')')
print(search(5, l))
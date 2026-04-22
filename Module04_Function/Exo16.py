
# validator purcentage.

def verifyInUndred(num) -> bool:
    if num <= 0 or num >= 100:
        raise Exception('num out of range')
    return True

print(verifyInUndred(10))
print(verifyInUndred(50))
print(verifyInUndred(150))
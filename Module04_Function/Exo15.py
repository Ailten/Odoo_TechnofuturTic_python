
# concat flexible.

def concat(*words: str, sep: str='-') -> str:  # ?? sep by default take ' '.
    return sep.join(words)

print(concat('a', 'b'))
print(concat('a', 'b', 'c'))
print(concat('a', 'b', 'c', sep='_'))
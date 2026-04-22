import re

# palendrome.

def isPalindrom(word) -> bool:
    return word == word[::-1]

def get_french_words() -> str:
    path_words = 'Module04_Function\\utils\\larousse2007.txt'
    bigest_palindrom = ''
    with open(path_words, 'r') as f:
        for l in f:
            word = l.strip()
            if not isPalindrom(word):
                continue
            if len(word) > len(bigest_palindrom):
                bigest_palindrom = word
    return bigest_palindrom

print(get_french_words())  # MALAYALAM
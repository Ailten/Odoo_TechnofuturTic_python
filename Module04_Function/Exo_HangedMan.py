import random
import re

# hanged man.

def get_french_words() -> str:
    output = None
    path_words = 'Module04_Function\\utils\\larousse2007.txt'
    list_words = []
    with open(path_words, 'r') as f:
        for l in f:
            list_words.append(l.strip())
    output = list_words[random.randint(0, len(list_words))]
    return output



# --- exec. ---
word_to_guess = get_french_words()
word_masked = [ (char, False) for char in word_to_guess ]

while True:

    print('')
    word_print = ' '.join([ (char[0] if char[1] else '_') for char in word_masked ])
    print(f"word : {word_print}")

    i = input('enter a letter.\n')

    char_match = re.search('^[a-z]$', i, re.I)
    if char_match == None:
        print('char not valide')
        continue

    char_ask = char_match.group(0).upper()

    if not (char_ask in word_to_guess):
        print("not this letter.")
        continue

    word_masked = [ 
        ((char[0], True) if (
            char[1] or char[0] == char_ask
        ) else char) 
        for char in word_masked 
    ]

    if len([ None for char in word_masked if not char[1] ]) == 0:
        print("you win !")
        print(f"word was {word_to_guess} !")
        break


    
    

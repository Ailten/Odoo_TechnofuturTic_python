import re

# count word identique on a sentence.

input_sentence = input("enter a sentence.\n")

words = re.findall('[^ ]{1,}', input_sentence)  # can be simplifie with split().
set_words = set(words)
dico_words = {w: words.count(w) for w in set_words}
print(dico_words)
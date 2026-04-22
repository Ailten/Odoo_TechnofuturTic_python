import re

# stats text.

def statsText(s: str) -> dict:
    return { 
        "words": len(s.split(' ')),
        "letters": len(re.findall('[^ ]', s))
    }

print(statsText('aaa bbb'))
print(statsText('a a a b'))
print(statsText('abbbaaa'))
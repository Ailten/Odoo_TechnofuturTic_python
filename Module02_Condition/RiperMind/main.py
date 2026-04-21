import random

# param.
amount_bomb = 10
size_map_x = 15
size_map_y = 10

class Bombs():
    bombs = []

# print screen.
def printScreen():
    for y in range(0, size_map_y, 1):
        str_line = ''
        for x in range(0, size_map_x, 1):
            bomb = (x, y)
            cel = '.'

            if findInBombs(bomb):
                cel = 'O'
            else:
                count_bomb_adj = countBombsAdj(bomb)
                if count_bomb_adj > 0:
                    cel = str(count_bomb_adj)

            str_line += cel
        print(str_line)

# generate bomb.
def generateBomb():
    print(Bombs.bombs)
    Bombs.bombs = []
    i = 0
    while i < amount_bomb:

        x = int(random.random() * size_map_x)
        y = int(random.random() * size_map_y)
        bomb = (x, y)

        if findInBombs(bomb):
            continue

        Bombs.bombs.append(bomb)
        i += 1

# find bombs.
def findInBombs(bomb) -> bool:
    for b in Bombs.bombs:
        if b[0] == bomb[0] and b[1] == bomb[1]:
            return True
    return False

# count bombs adjacent.
def countBombsAdj(pos) -> int:
    x = pos[0]
    y = pos[1]
    output = 0
    output += 1 if findInBombs((x-1, y-1)) else 0
    output += 1 if findInBombs((x-1, y  )) else 0
    output += 1 if findInBombs((x-1, y+1)) else 0
    output += 1 if findInBombs((x+1, y-1)) else 0
    output += 1 if findInBombs((x+1, y  )) else 0
    output += 1 if findInBombs((x+1, y+1)) else 0
    output += 1 if findInBombs((x  , y-1)) else 0
    output += 1 if findInBombs((x  , y+1)) else 0
    return output

# execute.
generateBomb()
printScreen()

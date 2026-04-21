import random

# param.
amount_bomb = 10
size_map_x = 15
size_map_y = 10

class RiperMind():
    bombs = []
    cels = []
    isLose = False

# print screen.
def printScreen():
    for y in range(len(RiperMind.cels)):
        str_line = ''
        for x in range(len(RiperMind.cels[y])):
            str_line += RiperMind.cels[y][x]['char'] if RiperMind.cels[y][x]['isFind'] else '#'


# generate bomb.
def generateBomb():
    RiperMind.bombs = []
    i = 0
    while i < amount_bomb:

        x = int(random.random() * size_map_x)
        y = int(random.random() * size_map_y)
        bomb = (x, y)

        if findInBombs(bomb):
            continue

        RiperMind.bombs.append(bomb)
        i += 1

# find bombs.
def findInBombs(bomb) -> bool:
    for b in RiperMind.bombs:
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

# generateCels.
def generateCels():
    RiperMind.cels = []
    for y in range(0, size_map_y, 1):
        RiperMind.cels.append([])
        for x in range(0, size_map_x, 1):
            bomb = (x, y)
            cel = '.'

            if findInBombs(bomb):
                cel = 'O'
            else:
                count_bomb_adj = countBombsAdj(bomb)
                if count_bomb_adj > 0:
                    cel = str(count_bomb_adj)

            RiperMind.cels[y].append({
                'char': cel,
                'isFind': False
            })

# try a pos.
def tryAPos(pos_try):
    if findInBombs(pos_try):
        RiperMind.isLose = True
        return
    revealACel(pos_try)
def revealACel(pos):
    if pos[0] < 0 or pos[0] >= size_map_x:
        return
    if pos[1] < 0 or pos[1] >= size_map_y:
        return
    cel = RiperMind.cels[pos[1]][pos[0]]
    if cel['isFind']:
        return
    RiperMind.cels[pos[1]][pos[0]]['isFInd'] = True
    if cel['char'] == '.':
        revealACel((pos[0]+1, pos[1]+1))  # FIXME: recursiv call to hight.
        revealACel((pos[0]+1, pos[1]  ))
        revealACel((pos[0]+1, pos[1]-1))
        revealACel((pos[0]-1, pos[1]+1))
        revealACel((pos[0]-1, pos[1]  ))
        revealACel((pos[0]-1, pos[1]-1))
        revealACel((pos[0]  , pos[1]+1))
        revealACel((pos[0]  , pos[1]-1))
    


# execute.
generateBomb()
generateCels()
printScreen()

while True:

    input_x = None
    input_y = None

    try:
        input_x = int(input("enter X pos to try.\n"))
        input_y = int(input("enter Y pos to try.\n"))
    except:
        print("an input enter is not a number !")  # verify number.
        continue

    # verify range.
    if input_x < 0 or input_x >= size_map_x:
        print("input X is out of range !")
        continue
    if input_y < 0 or input_y >= size_map_x:
        print("input Y is out of range !")
        continue

    pos_try = (input_x, input_y)
    tryAPos(pos_try)

    printScreen()

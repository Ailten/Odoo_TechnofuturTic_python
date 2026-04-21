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
        print(str_line)


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

# reveal all bombs.
def revealAllBombs():
    for b in RiperMind.bombs:
        RiperMind.cels[b[1]][b[0]]['isFind'] = True

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
def tryAPos(pos):
    if findInBombs(pos):
        RiperMind.isLose = True
        return
    RiperMind.cels[pos[1]][pos[0]]['isFInd'] = True
    current_wave_reveal = {pos_try}
    new_wave_reveal = set([])
    while True:
        for y in range(len(RiperMind.cels)):
            for x in range(len(RiperMind.cels[y])):
                cel = RiperMind.cels[y][x]
                if cel['isFind']:
                    continue
                if (x, y) in current_wave_reveal:
                    continue
                if len({e for e in current_wave_reveal if isAdj(e, (x, y)) and RiperMind.cels[e[1]][e[0]]['char'] == '.'}) > 0:
                    new_wave_reveal |= {(x, y)}
                    RiperMind.cels[y][x]['isFind'] = True  # TODO: it's not reveal when try work.
        if len(new_wave_reveal) == 0:
            break
            
def isAdj(posA, posB) -> bool:
    return abs(posA[0] - posB[0]) <= 1 or abs(posA[1] - posB[1]) <= 1

# is win.
def isWin() -> bool:
    for y in range(len(RiperMind.cels)):
        for x in range(len(RiperMind.cels[y])):
            c = RiperMind.cels[y][x]
            if c['char'] != 'O' and not c['isFind']:
                return False
    return True



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

    if RiperMind.isLose:
        revealAllBombs()
        print("you lose !")
        break
    if isWin():
        print("you won !")
        break

    printScreen()

print('end')
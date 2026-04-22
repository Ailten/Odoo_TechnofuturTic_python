from multiprocessing import Process
import keyboard
import time

# https://www.special-characters.com/p/brackets-special-character.html?m=1

# class Invader.
class Invader():
    def __init__(self):
        self.resolution = (20, 10)
        self.player = Entity(
            pos=(self.resolution[0] // 2, self.resolution[1] - 1),
            skin='︽'
        )
        self.time = 0

    def printScreen(self):
        line_str = ''
        for y in range(self.resolution[0]):
            line_str += '\n' if y != 0 else ''
            for x in range(self.resolution[1]):
                cel = ' '
                current_pos = (x, y)

                if Invader.comparePose(current_pos, self.player.pos):
                    cel = self.player.skin

                line_str += cel
        print(line_str)

    def update(self):
        self.time += 1
        
        time.sleep(0.017)  # 60 fps ~.

    @classmethod
    def comparePose(posA, posB) -> bool:
        return posA[0] == posB[0] and posA[1] == posB[1]

            

class Entity():
    def __init__(self, pos, skin='#'):
        self.pos = pos
        self.skin = skin


# --- execution --->
i = Invader()
while True:
    process = Process(target=i.update)
    process.start()
    while process.is_alive():
        if keyboard.is_pressed('q'):
            process.terminate()
    i.printScreen()
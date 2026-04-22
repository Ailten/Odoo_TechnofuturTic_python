from multiprocessing import Process
import keyboard  # python -m pip install
import time
import os
from functools import reduce

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
        self.ennemies = {

            # make a set from 2 loop imbricate.
            reduce(lambda a, b : (
                a | b
            ), ( 
                {(
                    { Entity((x, y), '︼') for y in range(0, 4)}
                ) for x in range(0, self.resolution[0] -1) })
            )

        }


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
        os.system('cls')
        print(line_str)

    def update(self):
        self.time += 1
        # TODO: move projectil and ennemies.
        time.sleep(0.017)  # 60 fps ~.

    @classmethod
    def comparePose(self, posA, posB) -> bool:
        return posA[0] == posB[0] and posA[1] == posB[1]

    def input(self, input_str):
        if input_str == 'up':
            pass # TODO: shoot.
        elif input_str == 'left':
            self.player.pos = (
                max(self.player.pos[0] - 1, 0),
                self.player.pos[1]
            )
        elif input_str == 'right':
            self.player.pos = (
                min(self.player.pos[0] + 1, self.resolution[0] - 1),
                self.player.pos[1]
            )

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
        is_left = keyboard.is_pressed('q')
        is_right = keyboard.is_pressed('d')
        is_up = keyboard.is_pressed('z')
        if (
            is_left or is_right or is_up
        ):
            if is_left:
                i.input('left')
            if is_right:
                i.input('right')
            if is_up:
                i.input('up')
            process.terminate()
    i.printScreen()
import numpy
import threading
import time
import sys
#import curses
from colorama import just_fix_windows_console
from colorama import Fore, Style


board_state = numpy.array([
[['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']],
[['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']],
[['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']],
[['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]])

board = f"""
             _ _ _ _ _ _ _ _ _ _
            |{board_state[0,0,0]}|{board_state[0,0,1]}|{board_state[0,0,2]}|{board_state[0,0,3]}|{board_state[0,0,4]}|{board_state[0,0,5]}|{board_state[0,0,6]}|{board_state[0,0,7]}|{board_state[0,0,8]}|{board_state[0,0,9]}|
            |{board_state[0,0,10]}|{board_state[0,0,11]}|{board_state[0,0,12]}|{board_state[0,0,13]}|{board_state[0,0,14]}|{board_state[0,0,15]}|{board_state[0,0,16]}|{board_state[0,1,0]}|{board_state[0,1,1]}|{board_state[0,1,2]}|
            |{board_state[0,1,3]}|{board_state[0,1,4]}|{board_state[0,1,5]}|{board_state[0,1,6]}|{board_state[0,1,7]}|{board_state[0,1,8]}|{board_state[0,1,9]}|{board_state[0,1,10]}|{board_state[0,1,11]}|{board_state[0,1,12]}|
            |{board_state[0,1,13]}|{board_state[0,1,14]}|{board_state[0,1,15]}|{board_state[0,1,16]}|{board_state[0,2,0]}|{board_state[0,2,1]}|{board_state[0,2,2]}|{board_state[0,2,3]}|{board_state[0,2,4]}|{board_state[0,2,5]}|
            |{board_state[0,2,6]}|{board_state[0,2,7]}|{board_state[0,2,8]}|{board_state[0,2,9]}|{board_state[0,2,10]}|{board_state[0,2,11]}|{board_state[0,2,12]}|{board_state[0,2,13]}|{board_state[0,2,14]}|{board_state[0,2,15]}|
 _ _ _ _ _ _|{board_state[0,2,16]}|{board_state[0,3,0]}|{board_state[0,3,1]}|{board_state[0,3,2]}|{board_state[0,3,3]}|{board_state[0,3,4]}|{board_state[0,3,5]}|{board_state[0,3,6]}|{board_state[0,3,7]}|{board_state[0,3,8]}|_ _ _ _ _ _
|{board_state[0,3,9]}|{board_state[0,3,10]}|{board_state[0,3,11]}|{board_state[0,3,12]}|{board_state[0,3,13]}|{board_state[0,3,14]}|{board_state[0,3,15]}|{board_state[0,3,16]}|{board_state[0,4,0]}|{board_state[0,4,1]}|{board_state[0,4,2]}|{board_state[0,4,3]}|{board_state[0,4,4]}|{board_state[0,4,5]}|{board_state[0,4,6]}|{board_state[0,4,7]}|{board_state[0,4,8]}|{board_state[0,4,9]}|{board_state[0,4,10]}|{board_state[0,4,11]}|{board_state[0,4,12]}|{board_state[0,4,13]}|
|{board_state[0,4,14]}|{board_state[0,4,15]}|{board_state[0,4,16]}|{board_state[1,0,0]}|{board_state[1,0,1]}|{board_state[1,0,2]}|{board_state[1,0,3]}|{board_state[1,0,4]}|{board_state[1,0,5]}|{board_state[1,0,6]}|{board_state[1,0,7]}|{board_state[1,0,8]}|{board_state[1,0,9]}|{board_state[1,0,10]}|{board_state[1,0,11]}|{board_state[1,0,12]}|{board_state[1,0,13]}|{board_state[1,0,14]}|{board_state[1,0,15]}|{board_state[1,0,16]}|{board_state[1,1,0]}|{board_state[1,1,1]}|
|{board_state[1,1,2]}|{board_state[1,1,3]}|{board_state[1,1,4]}|{board_state[1,1,5]}|{board_state[1,1,6]}|{board_state[1,1,7]}|{board_state[1,1,8]}|{board_state[1,1,9]}|{board_state[1,1,10]}|{board_state[1,1,11]}|{board_state[1,1,12]}|{board_state[1,1,13]}|{board_state[1,1,14]}|{board_state[1,1,15]}|{board_state[1,1,16]}|{board_state[1,2,0]}|{board_state[1,2,1]}|{board_state[1,2,2]}|{board_state[1,2,3]}|{board_state[1,2,4]}|{board_state[1,2,5]}|{board_state[1,2,6]}|
|{board_state[1,2,7]}|{board_state[1,2,8]}|{board_state[1,2,9]}|{board_state[1,2,10]}|{board_state[1,2,11]}|{board_state[1,2,12]}|{board_state[1,2,13]}|{board_state[1,2,14]}|{board_state[1,2,15]}|{board_state[1,2,16]}|{board_state[1,3,0]}|{board_state[1,3,1]}|{board_state[1,3,2]}|{board_state[1,3,3]}|{board_state[1,3,4]}|{board_state[1,3,5]}|{board_state[1,3,6]}|{board_state[1,3,7]}|{board_state[1,3,8]}|{board_state[1,3,9]}|{board_state[1,3,10]}|{board_state[1,3,11]}|
|{board_state[1,3,12]}|{board_state[1,3,13]}|{board_state[1,3,14]}|{board_state[1,3,15]}|{board_state[1,3,16]}|{board_state[1,4,0]}|{board_state[1,4,1]}|{board_state[1,4,2]}|{board_state[1,4,3]}|{board_state[1,4,4]}|{board_state[1,4,5]}|{board_state[1,4,6]}|{board_state[1,4,7]}|{board_state[1,4,8]}|{board_state[1,4,9]}|{board_state[1,4,10]}|{board_state[1,4,11]}|{board_state[1,4,12]}|{board_state[1,4,13]}|{board_state[1,4,14]}|{board_state[1,4,15]}|{board_state[1,4,16]}|
|{board_state[2,0,0]}|{board_state[2,0,1]}|{board_state[2,0,2]}|{board_state[2,0,3]}|{board_state[2,0,4]}|{board_state[2,0,5]}|{board_state[2,0,6]}|{board_state[2,0,7]}|{board_state[2,0,8]}|{board_state[2,0,9]}|{board_state[2,0,10]}|{board_state[2,0,11]}|{board_state[2,0,12]}|{board_state[2,0,13]}|{board_state[2,0,14]}|{board_state[2,0,15]}|{board_state[2,0,16]}|{board_state[2,1,0]}|{board_state[2,1,1]}|{board_state[2,1,2]}|{board_state[2,1,3]}|{board_state[2,1,4]}|
|{board_state[2,1,5]}|{board_state[2,1,6]}|{board_state[2,1,7]}|{board_state[2,1,8]}|{board_state[2,1,9]}|{board_state[2,1,10]}|{board_state[2,1,11]}|{board_state[2,1,12]}|{board_state[2,1,13]}|{board_state[2,1,14]}|{board_state[2,1,15]}|{board_state[2,1,16]}|{board_state[2,2,0]}|{board_state[2,2,1]}|{board_state[2,2,2]}|{board_state[2,2,3]}|{board_state[2,2,4]}|{board_state[2,2,5]}|{board_state[2,2,6]}|{board_state[2,2,7]}|{board_state[2,2,8]}|{board_state[2,2,9]}|
|{board_state[2,2,10]}|{board_state[2,2,11]}|{board_state[2,2,12]}|{board_state[2,2,13]}|{board_state[2,2,14]}|{board_state[2,2,15]}|{board_state[2,2,16]}|{board_state[2,3,0]}|{board_state[2,3,1]}|{board_state[2,3,2]}|{board_state[2,3,3]}|{board_state[2,3,4]}|{board_state[2,3,5]}|{board_state[2,3,6]}|{board_state[2,3,7]}|{board_state[2,3,8]}|{board_state[2,3,9]}|{board_state[2,3,10]}|{board_state[2,3,11]}|{board_state[2,3,12]}|{board_state[2,3,13]}|{board_state[2,3,14]}|
|{board_state[2,3,15]}|{board_state[2,3,16]}|{board_state[2,4,0]}|{board_state[2,4,1]}|{board_state[2,4,2]}|{board_state[2,4,3]}|{board_state[2,4,4]}|{board_state[2,4,5]}|{board_state[2,4,6]}|{board_state[2,4,7]}|{board_state[2,4,8]}|{board_state[2,4,9]}|{board_state[2,4,10]}|{board_state[2,4,11]}|{board_state[2,4,12]}|{board_state[2,4,13]}|{board_state[2,4,14]}|{board_state[2,4,15]}|{board_state[2,4,16]}|{board_state[3,0,0]}|{board_state[3,0,1]}|{board_state[3,0,2]}|
|{board_state[3,0,3]}|{board_state[3,0,4]}|{board_state[3,0,5]}|{board_state[3,0,6]}|{board_state[3,0,7]}|{board_state[3,0,8]}|{board_state[3,0,9]}|{board_state[3,0,10]}|{board_state[3,0,11]}|{board_state[3,0,12]}|{board_state[3,0,13]}|{board_state[3,0,14]}|{board_state[3,0,15]}|{board_state[3,0,16]}|{board_state[3,1,0]}|{board_state[3,1,1]}|{board_state[3,1,2]}|{board_state[3,1,3]}|{board_state[3,1,4]}|{board_state[3,1,5]}|{board_state[3,1,6]}|{board_state[3,1,7]}|
            |{board_state[3,1,8]}|{board_state[3,1,9]}|{board_state[3,1,10]}|{board_state[3,1,11]}|{board_state[3,1,12]}|{board_state[3,1,13]}|{board_state[3,1,14]}|{board_state[3,1,15]}|{board_state[3,1,16]}|{board_state[3,2,0]}|
            |{board_state[3,2,1]}|{board_state[3,2,2]}|{board_state[3,2,3]}|{board_state[3,2,4]}|{board_state[3,2,5]}|{board_state[3,2,6]}|{board_state[3,2,7]}|{board_state[3,2,8]}|{board_state[3,2,9]}|{board_state[3,2,10]}|
            |{board_state[3,2,11]}|{board_state[3,2,12]}|{board_state[3,2,13]}|{board_state[3,2,14]}|{board_state[3,2,15]}|{board_state[3,2,16]}|{board_state[3,3,0]}|{board_state[3,3,1]}|{board_state[3,3,2]}|{board_state[3,3,3]}|
            |{board_state[3,3,4]}|{board_state[3,3,5]}|{board_state[3,3,6]}|{board_state[3,3,7]}|{board_state[3,3,8]}|{board_state[3,3,9]}|{board_state[3,3,10]}|{board_state[3,3,11]}|{board_state[3,3,12]}|{board_state[3,3,13]}|
            |{board_state[3,3,14]}|{board_state[3,3,15]}|{board_state[3,3,16]}|{board_state[3,4,0]}|{board_state[3,4,1]}|{board_state[3,4,2]}|{board_state[3,4,3]}|{board_state[3,4,4]}|{board_state[3,4,5]}|{board_state[3,4,6]}|
            |{board_state[3,4,7]}|{board_state[3,4,8]}|{board_state[3,4,9]}|{board_state[3,4,10]}|{board_state[3,4,11]}|{board_state[3,4,12]}|{board_state[3,4,13]}|{board_state[3,4,14]}|{board_state[3,4,15]}|{board_state[3,4,16]}|"""

print(board)

class Block:

    def __init__(self, name, structnum, direction, center):
        self.name = name
        if structnum == 1:
            self.struct = '2X2'
        elif structnum == 2:
            self.struct = 'R_ZIG'
        elif structnum == 3:
            self.struct = 'L_ZIG'
        elif structnum == 4:
            self.struct = 'LINE'
        elif structnum == 5:
            self.struct = 'LL'
        elif structnum == 6:
            self.struct = 'RL'
        else:
            self.struct = 'T'
        self.orientation = "UP"
        self.direction = direction
        self.center = center

    def falling(self):
        direction = self.direction
        if direction == 'DOWN':
            center = center + [0, 0, 10]
            if center > [0, 0, 16]:
                center = center + [0, 1, -17]
                if center > [0, 4, 0]:
                    center = center [1, -5, 0]
        elif direction == 'LEFT':
            center = center + [0, 0, -1]
            if center < [0, 0, 0]:
                center = center + [0, -1, 16]
                if center < [0, 0, 0]:
                    center = center + [-1, 4, 0]
        elif direction == "RIGHT":
            center = center + [0, 0, 1]
            if center > [0, 0, 16]:
                center = center + [0, 1, -17]
                if center > [0, 4, 0]:
                    center = center + [1, 0, 0]
        else:
            center = center + [0, 0, -10]
            if center < [0, 0, 0]:
                center = center + [0, -1, 5]
                if center < [0, 4, 0]:
                    center = center [-1, 4, 0]



    fallthread = threading.Thread(target= falling())
    fallthread.start()
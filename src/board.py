# ========================================================================
# File: board.py
# Date: 15-10-2020
# Creator: Asaad Abbasii 
# Notice: (C) Copyright 2020 by Asaad Noman Abbasi All Rights Reserved. 
#========================================================================

import pygame
from letter import Letter

class Board:

    def __init__(self):
        self.x = 50
        self.y = 50
        self.rc = 15
        self.puzzle = [[0 for x in range(self.rc)] for y in range(self.rc)]
        xx = self.x
        yy = self.y
        letterSize = 50
        for i in range(0,self.rc):
            for j in range(0,self.rc):
                self.puzzle[i][j] = Letter(xx,yy,letterSize,letterSize)
                xx += letterSize
            xx = self.x
            yy += letterSize

    def render(self,window):
        for i in range(self.rc):
            for j in range(self.rc):
                self.puzzle[i][j].render(window)

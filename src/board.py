# ========================================================================
# File: board.py
# Date: 15-10-2020
# Creator: Asaad Abbasi
# Notice: (C) Copyright 2020 by Asaad Noman Abbasi All Rights Reserved. 
#========================================================================

import pygame
from letter import *

class Board:

    drag = False

    def __init__(self):
        self.x = 50
        self.y = 60
        self.rc = 15
        self.puzzle = [[0 for x in range(self.rc)] for y in range(self.rc)]
        xx = self.x
        yy = self.y
        letterSize = 50
        for i in range(0,self.rc):
            for j in range(0,self.rc):
                self.puzzle[i][j] = BoardLetter(xx,yy,letterSize,letterSize)
                xx += letterSize
            xx = self.x
            yy += letterSize

        self.generatedwordsText = Font("Comic Sans MS","Generated Words",900,self.y,30)
        self.currentSelectedWords = []

    def update(self,e):
        if e.type == pygame.MOUSEBUTTONDOWN:
           self.drag = True
        elif e.type == pygame.MOUSEMOTION:
            if self.drag:
                for i in range(15):
                    for j in range(15):
                        #do not let draggin go on for more then the word size limit
                        if len(self.currentSelectedWords) == 7:
                            self.drag = False
                        if self.puzzle[j][i].checkCollision(e.pos):
                            if self.puzzle[j][i].isFilled() == False: #avoid duplication in list
                                self.currentSelectedWords.append(self.puzzle[j][i].getData())
                            self.puzzle[j][i].fill(True)
                            break

        elif e.type == pygame.MOUSEBUTTONUP:
            self.drag = False
            for i in range(15):
                for j in range(15):
                    if self.puzzle[j][i].isFilled():
                        self.puzzle[j][i].fill(False)
            print(self.currentSelectedWords)
            self.currentSelectedWords.clear()

    def render(self,window):
        self.generatedwordsText.render(window)
        for i in range(self.rc):
            for j in range(self.rc):
                self.puzzle[i][j].render(window)

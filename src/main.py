# ========================================================================
# File: main.py
# Date: 15-10-2020
# Creator: Asaad Abbasii 
# Notice: (C) Copyright 2020 by Asaad Noman Abbasi All Rights Reserved. 
#========================================================================

import pygame
from board import Board

class WordSearch:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Word-Search")
        self.window = pygame.display.set_mode((1250,900))
        running = True
        clock = pygame.time.Clock()

        self.board = Board()

        while running:
            clock.tick(60)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False

            self.render()

    def render(self):
        self.window.fill((255,255,255))
        self.board.render(self.window)
        pygame.display.update()

game = WordSearch()
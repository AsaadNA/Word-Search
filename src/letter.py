# ========================================================================
# File: board.py
# Date: 16-10-2020
# Creator: Asaad Abbasii 
# Notice: (C) Copyright 2020 by Asaad Noman Abbasi All Rights Reserved. 
#========================================================================

import pygame
import random

class Letter:

    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.data = "A"
        font = pygame.font.SysFont("Consolas",30)
        self.fontSurface = font.render(self.data,False,(0,0,0))
        
        self.r = random.randint(100,255)
        self.g = random.randint(100,255)
        self.b = random.randint(100,255)
    
    def render(self,window):
        #pygame.draw.rect(window,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))
        window.blit(self.fontSurface,(self.x + 17,self.y + 8))

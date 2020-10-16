# ========================================================================
# File: letter.py
# Date: 16-10-2020
# Creator: Asaad Abbasi 
# Notice: (C) Copyright 2020 by Asaad Noman Abbasi All Rights Reserved. 
#========================================================================

import pygame,random

class Font:
    def __init__(self,fontName,text,x,y,size):
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(fontName,size)
        self.surface = self.font.render(text,False,(0,0,0))
    def setText(self,text):
        self.surface = self.font.render(text,False,(0,0,0))
    def render(self,window):
        window.blit(self.surface,(self.x,self.y))

class BoardLetter:

    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        randomChar = random.randint(97,122)
        self.data = chr(randomChar)
        self.font = Font("Consolas",self.data,self.x+17,self.y+10,30)
        self.fillColor = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
        self.fillRect = False
        self.boundaryRect = pygame.rect.Rect(self.x+10,self.y+10,self.w-20,self.h-20)

    def checkCollision(self,mousePoint):
        return (self.boundaryRect.collidepoint(mousePoint))

    def setData(self,data):
        self.font.setText(data)

    def getData(self):
        return self.data
    
    def fill(self,flag):
        self.fillRect = flag

    def isFilled(self):
        return self.fillRect

    def render(self,window):
        if self.fillRect:
            pygame.draw.rect(window,self.fillColor,(self.x,self.y,self.w,self.h))
        self.font.render(window)

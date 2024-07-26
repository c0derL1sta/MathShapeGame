import pygame
import math
import random

class mainAtk(pygame.sprite.Sprite):
    def __init__(self, Xpos, Ypos):
        pygame.sprite.Sprite.__init__(self)
        self.isDone = False
        
        self.x = Xpos
        self.y = Ypos

        #Spawn attack with same cordinates 

        #Spawn hint randomly that has a random

        
    
    def getIsCompleted(self):
        return self.isDone
    
    def attack(self):
        if not self.isDone:
            #Create the 3 random  raidus line with a random angle between 0 and 2pi radians
            #This will create the 3 hint nodes
            line1 = 0

    def update(self):
        self.attack()

class atkNode():
    pass

class hintNode(pygame.sprite.Sprite):
    def __init__(self):
        pass

class deathCircle:
    pass
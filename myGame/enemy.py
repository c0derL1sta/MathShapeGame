import pygame
import math

class mainAtk(pygame.sprite.Sprit):
    def __init__(self, Xpos, Ypos):
        pygame.sprite.Sprite.__init__(self)
        self.isDone = False
        
        self.x = Xpos
        self.y = Ypos

        #Spawn hintNode with same cordinates 

        #Spawn atkNode randomly that has a random
    
    def getIsCompleted(self):
        return self.isDone

class atkNode:
    pass

class hintNode:
    pass

class deathCircle:
    pass
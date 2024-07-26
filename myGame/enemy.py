import pygame
import math
import random

from pygame.sprite import _Group

class mainAtk(pygame.sprite.Sprite):
    def __init__(self, Xpos, Ypos):
        pygame.sprite.Sprite.__init__(self)
        self.isDone = False
        
        self.x = Xpos
        self.y = Ypos

        #For the attack node distance from hint node
        self.MIN_RANGE = 10
        self.MAX_RANGE = 200

        #Spawn attack with same cordinates 

        #Spawn hint randomly that has a random

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getIsCompleted(self):
        return self.isDone
    
    def attack(self):
        if not self.isDone:
            #Create the 3 random  raidus line with a random angle between 0 and 2pi radians
            #This will create the 3 hint nodes
            line1 = random.randint(0, self.MAX_RANGE)
            line2 = random.randint(0, self.MAX_RANGE)
            line3 = random.randint(0, self.MAX_RANGE)

            #Atk Node
            self.atkNode1 = atkNode()



    def update(self):
        self.attack()

class atkNode(pygame.sprite.Sprite):
    def __init__(self, mainAtk):
        pygame.sprite.Sprite.__init__(self)
        self.xPos = mainAtk.getX()
        self.yPos = mainAtk.getY()
    
    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos

class hintNode(pygame.sprite.Sprite):
    def __init__(self, atkNode, RADIUS_HYPO_LINE):
        pygame.sprite.Sprite.__init__(self)

        """
        Basically next to vars heres what happens
        we want a hint node with d radius distance from the atk node
        we want to 'rotate' it around the radius by a random radian between 0 and 2 pi
        """
        self.theta = random.uniform(0, 2 * math.pi)
        self.xPos = round(atkNode.getX() + math.cos(self.theta) * RADIUS_HYPO_LINE)
        self.yPos = round(atkNode.getY() + math.sin(self.theta) * RADIUS_HYPO_LINE)
        
class deathCircle:
    pass

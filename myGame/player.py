import pygame
import os

# classes for our game objects
class player(pygame.sprite.Sprite):
    def __init__(self, game, xPos, yPos):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,50])
        self.image.fill([255,0,0])
        self.rect = self.image.get_rect()

        self.game = game
        self.x = xPos
        self.y = yPos

    def move(self):
        # Handle Input Events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 50
        if keys[pygame.K_s]:
            self.y += 50
        if keys[pygame.K_a]:
            self.x -= 50
        if keys[pygame.K_d]:
            self.x += 50
    
    def preventLeavingScreen(self):
        #A prevention measure to keep player inside the 'screen' and not going out of sight
        
        #Dont go to far left
        if(self.x < 0):
            self.x = 0
        
        #Dont go to far right , subtract player's width so it doesnt look part of it is off the screen
        elif(self.x > 1000):
            self.x = 1000 - self.image.get_width()
        
        #Dont go to far up, 
        elif(self.y < 0):
            self.y = 0
        
        #Dont go to far down, subtract player's height so it doesnt look a part of it is off
        elif(self.y > 800):
            self.y = 800 - self.image.get_height()


    def update(self):
        self.move()
        self.preventLeavingScreen()
        self.rect.x = self.x
        self.rect.y = self.y
        


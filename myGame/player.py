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

        self.playerSpeed = 15

    def move(self):
        # Handle Input Events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.playerSpeed
        if keys[pygame.K_s]:
            self.y += self.playerSpeed
        if keys[pygame.K_a]:
            self.x -= self.playerSpeed
        if keys[pygame.K_d]:
            self.x += self.playerSpeed
    
    def preventLeavingScreen(self):
        #A prevention measure to keep player inside the 'screen' and not going out of sight
        
        #Dont go to far left
        if(self.x < 0):
            self.x = 0
        
        #Dont go to far right , subtract player's width so it doesnt look part of it is off the screen
        if(self.x > 950):
            self.x = 950
        
        #Dont go to far up, 
        if(self.y < 0):
            self.y = 0
        
        #Dont go to far down, subtract player's height so it doesnt look a part of it is off
        if(self.y > 750):
            self.y = 750


    def update(self):
        self.move()
        self.preventLeavingScreen()
        self.rect.x = self.x
        self.rect.y = self.y
        


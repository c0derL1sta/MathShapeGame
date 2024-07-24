import pygame
import os

# classes for our game objects
class player(pygame.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""

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
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.y += 100

    def update(self):
        self.move()


import pygame
import os

# classes for our game objects
class player(pygame.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""

    def __init__(self, game, xPos, yPos):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = pygame.rect
        self.fist_offset = (-235, -80)
        self.punching = False

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


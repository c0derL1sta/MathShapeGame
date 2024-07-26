# Import Modules
import os
import pygame
import player
import sys
import random

from config import *

class game:
    def __init__(self):
        """this function is called when the program starts.
        it initializes everything it needs, then runs in
        a loop until the function returns."""
        # Initialize Everything
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        pygame.display.set_caption("Math Shape survival")
        pygame.mouse.set_visible(False)

        # Create The Background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(GREEN)


        #Create the sprite
        self.player = player.player(self,0,0)

        #Put sprites into groups to render
        self.allsprites = pygame.sprite.Group((self.player))

        #Clock feature
        self.clock = pygame.time.Clock()

        #Random Timer 1: This will activate randomly every 3 to 10 seconds
        # Define a custom event type for the timer
        self.TIMER_EVENT = pygame.USEREVENT + 1

        # Define the range for the 2nd attack delay timer (in milliseconds)
        self.MIN_INTERVAL = 3000  # Minimum interval (3 second)
        self.MAX_INTERVAL = 8000  # Maximum interval (8 seconds) 

        self.isAtk = False

    """
    Code for the first random timer, this is the timer that activate every so ofter
    that will start the attack process, this will spawn the atk node and 1 hint node
    starting the process
    """
    def set_random_timer(self):
        #print("1") #this func is called
        interval = random.randint(self.MIN_INTERVAL, self.MAX_INTERVAL)
        pygame.time.set_timer(self.TIMER_EVENT, interval)

    #Setup for the 2nd timer when the first timer activates 
    #This is the func that starts the attack thing
    def timer_callback(self):
        #print("3") #Func works
        #print("Random timer triggered!AKAK ATTACK PROCESS NOW")

        #Make sure theres only one attack
        self.isAtk = True

        #Setup vars for the attack thing
        atkXpos = random.randint(0, SCREEN_WIDTH)
        atkYPos = random.randint(0, SCREEN_HEIGHT)

        #Start the attack
        #call the main Atk object
        #Input: Random Xpos and Ypos


    def main(self):
        """this function is called when the program starts.
        it initializes everything it needs, then runs in
        a loop until the function returns."""

        # Main Loop
        playing = True

        self.set_random_timer() #Starts the first random timer that is an event

        while playing:
            self.clock.tick(60)

            # Handle Input Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    playing = False
                if event.type == self.TIMER_EVENT:
                    if not self.isAtk:
                        self.timer_callback()
                        #print("2") #Func not called which means no timer
                    else:
                        #print("No attky ")
                        pass
            """"
            Call the is Atk done func that does all of this
            Check if the attack object is done 
            Check if the attack is done to activate the attack process again
            if self.manatkObj.getIsCompleted() <-this should return a bool: self.isAtk = false
            or self.isAtk = the opposite of self.manatkObj.getIsCompleted()
            getIscomplete = true which means its done making isAtk false
            and vice versa
            """


            # Draw Everything
            #first the screen then sprites ontop
            self.screen.blit(self.background, (0, 0))
            self.allsprites.update() #Update all them sprites
            self.allsprites.draw(self.screen)
            pygame.display.flip()

        pygame.quit()


g = game()
g.main()
os._exit(0)

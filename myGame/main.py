# Import Modules
import os
import pygame
import player

class game:
    def __init__(self):
        """this function is called when the program starts.
        it initializes everything it needs, then runs in
        a loop until the function returns."""
        # Initialize Everything
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Math Shape survival")
        pygame.mouse.set_visible(False)

        # Create The Background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((170, 238, 187))


        #Create the sprite
        self.player = player.player(self,0,0)

        #Put sprites into groups to render
        self.allsprites = pygame.sprite.Group((self.player))

        #Clock fature
        self.clock = pygame.time.Clock()

    def test_say_hi():
        print("yeet")

    def main(self):
        """this function is called when the program starts.
        it initializes everything it needs, then runs in
        a loop until the function returns."""

        # Main Loop
        playing = True
        while playing:
            self.clock.tick(60)

            # Handle Input Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    playing = False
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                    pass

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

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
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((170, 238, 187))

        # Display The Background
        self.screen.blit(background, (0, 0))
        pygame.display.flip()

        #render player sprite?
        self.player = player.player(self,900,800)
        self.clock = pygame.time.Clock()

    def main(self):
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

        # Display The Background
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        #render spirte?
        self.allsprites = pygame.sprite.RenderPlain((self.player))


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

            #Update all them sprites
            self.allsprites.update()

            # Draw Everything
            self.screen.blit(self.background, (0, 0))
            self.allsprites.draw(self.screen)
            pygame.display.flip()

        playing.quit()


g = game()
g.main()
os.exit()

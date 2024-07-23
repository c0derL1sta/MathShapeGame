# Import Modules
import os
import pygame
import player

def main():
    """this function is called when the program starts.
    it initializes everything it needs, then runs in
    a loop until the function returns."""
    # Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Math Shape survival")
    pygame.mouse.set_visible(False)

    # Create The Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #render spirte?
    player = player.player(player,900,800)
    allsprites = pygame.sprite.RenderPlain((player))
    clock = pygame.time.Clock()


    # Main Loop
    playing = True
    while playing:
        clock.tick(60)

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                playing = False

        #Update all them sprites
        allsprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        playing.display.flip()

    playing.quit()


if __name__ == '__main__': main()
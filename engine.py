import pygame
from __init__ import initialize_game
from config import *

def main():
    # Initialize Pygame and game entities
    screen, clock = initialize_game()

    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # User input handling (you might want to add more advanced input handling)
        keys = pygame.key.get_pressed()

        # Update game state
        # all_sprites.update()

        # Draw graphics
        screen.fill(BACKGROUND_COLOR)  # Fill the screen with a black color (adjust as needed)
        # all_sprites.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Control the frame rate
        clock.tick(FRAMERATE)  # Adjust the frame rate as needed

    pygame.quit()

if __name__ == "__main__":
    main()
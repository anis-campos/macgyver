import pygame

from gui import BLUE


class Level:
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self):
        """ Constructor. Pass in a handle to player. """

        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.cell_list = None

        # Background image
        self.background = None

        self.cell_list = pygame.sprite.Group()

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.cell_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(BLUE)

        # Draw all the sprite lists that we have
        self.cell_list.draw(screen)

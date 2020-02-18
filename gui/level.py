import pygame

from gui import constants
from gui.constants import BLOCK_SIZE
from labyrinth import Labyrinth, CellType
from gui.cell import Wall, Floor, FloorType


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
        screen.fill(constants.BLUE)

        # Draw all the sprite lists that we have
        self.cell_list.draw(screen)


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self)

        # Array with type of platform, and x, y location of the platform.
        self.lab = Labyrinth()
        self.lab.load('../level_1')

        # Go through the array above and add platforms
        for cell in self.lab.mazeMap:

            if cell.type == CellType.WALL:
                cell_gui = Wall()
            elif cell.type == CellType.HALL:
                cell_gui = Floor()
            elif cell.type == CellType.START:
                cell_gui = Floor(floor_type=FloorType.START)
            elif cell.type == CellType.END:
                cell_gui = Floor(floor_type=FloorType.END)
            else:
                continue
            cell_gui.rect.x = cell.x * BLOCK_SIZE
            cell_gui.rect.y = cell.y * BLOCK_SIZE
            self.cell_list.add(cell_gui)

        self.walls = [cell for cell in self.cell_list if isinstance(cell, Wall)]

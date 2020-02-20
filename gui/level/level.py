import pygame
from pygame.sprite import Group

from gui import BLUE, BLOCK_SIZE
from gui.tiles.floor import Floor
from gui.tiles.floor_type import FloorType
from gui.tiles.wall import Wall
from model.labyrinth import Labyrinth, CellType


class Level:
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    _labyrinth: Labyrinth

    """
         Lists of sprites used in all levels. 
    """
    cell_list: Group

    def __init__(self, level_file_name: str = None):
        """ Constructor. Pass in a handle to player. """

        self.cell_list = pygame.sprite.Group()

        # Loading level file
        self._labyrinth = Labyrinth()
        self._labyrinth.load(level_file_name)

        # Go through the array above and add platforms
        for cell in self._labyrinth.mazeMap:

            if cell.type == CellType.WALL:
                cell_gui = Wall()
            elif cell.type == CellType.HALL:
                cell_gui = Floor()
            elif cell.type == CellType.START:
                cell_gui = Floor(floor_type=FloorType.START)
                self.start = cell_gui
            elif cell.type == CellType.END:
                cell_gui = Floor(floor_type=FloorType.END)
                self.end = cell_gui
            else:
                continue
            cell_gui.rect.x = cell.x * BLOCK_SIZE
            cell_gui.rect.y = cell.y * BLOCK_SIZE
            self.cell_list.add(cell_gui)

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

    _walls: list = None

    @property
    def walls(self):
        if self._walls is None:
            self._walls = [cell for cell in self.cell_list if isinstance(cell, Wall)]
        return self._walls

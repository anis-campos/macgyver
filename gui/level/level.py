import pygame
from pygame.sprite import Group

from gui import BLUE, BLOCK_SIZE
from gui.tiles.floor import Floor
from gui.tiles.floor_type import FloorType
from gui.tiles.wall import Wall
from model.labyrinth import Labyrinth, TileType


class Level:
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    _labyrinth: Labyrinth

    @property
    def guardian(self):
        raise NotImplemented

    """
         Lists of sprites used in all levels. 
    """
    tile_list: Group

    def __init__(self, level_file_name: str = None):
        """ Constructor. Pass in a handle to player. """

        self.tile_list = pygame.sprite.Group()

        # Loading level file
        self._labyrinth = Labyrinth()
        self._labyrinth.load(level_file_name)

        # Go through the array above and add platforms
        for tile in self._labyrinth.mazeMap:
            if tile.type == TileType.WALL:
                tile_gui = Wall(tile)
            elif tile.type == TileType.HALL:
                tile_gui = Floor(tile)
            elif tile.type == TileType.START:
                tile_gui = Floor(tile,floor_type=FloorType.START)
                self.start = tile_gui
            elif tile.type == TileType.END:
                tile_gui = Floor(tile,floor_type=FloorType.END)
                self.end = tile_gui
            else:
                continue

            self.tile_list.add(tile_gui)

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.tile_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(BLUE)

        # Draw all the sprite lists that we have
        self.tile_list.draw(screen)

    _walls: list = None

    @property
    def walls(self):
        if self._walls is None:
            self._walls = [tile for tile in self.tile_list if isinstance(tile, Wall)]
        return self._walls

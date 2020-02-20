from gui.level import LEVEL01
from gui.level.level import Level
from model.labyrinth import Tile


class Level01(Level):
    """ Definition for level 1. """

    def __init__(self):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, LEVEL01)

    @property
    def guardian(self) -> Tile:
        return Tile(self.end.tile.x, self.end.tile.y + 1)

from gui import BLOCK_SIZE
from gui.level.level import Level
from gui.tiles.floor import Floor
from gui.tiles.floor_type import FloorType
from gui.tiles.wall import Wall
from model.labyrinth import Labyrinth, CellType


class Level01(Level):
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
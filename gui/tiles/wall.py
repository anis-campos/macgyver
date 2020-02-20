from gui.images.sprite import Sprite
from gui.images.spritesheet import SpriteSheet
from gui.resource.tile_mapping import WALL_DEFAULT
from gui.tiles.tile_gui import TileGui
from gui.tiles.wall_type import WallType
from model.labyrinth import Tile


class Wall(TileGui):
    _switcher = {WallType.DEFAULT: WALL_DEFAULT}

    def __init__(self, tile: Tile, wall_type: WallType = WallType.DEFAULT):
        self.wall_type = wall_type
        super().__init__(tile)

    @property
    def sprite_sheet(self) -> SpriteSheet:
        return self.loader.SHEET_WALL

    @property
    def sprite(self) -> Sprite:
        return self._switcher[self.wall_type]

    def __str__(self):
        return "{}".format(self.rect)

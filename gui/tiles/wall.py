from gui.images.sprite import Sprite
from gui.images.spritesheet import SpriteSheet
from gui.resource.tile_mapping import WALL_DEFAULT
from gui.tiles.tile import Tile
from gui.tiles.wall_type import WallType


class Wall(Tile):
    _switcher = {WallType.DEFAULT: WALL_DEFAULT}

    def __init__(self, wall_type: WallType = WallType.DEFAULT):
        self.wall_type = wall_type
        super().__init__()

    @property
    def sprite_sheet(self) -> SpriteSheet:
        return self.loader.SHEET_WALL

    @property
    def sprite(self) -> Sprite:
        return self._switcher[self.wall_type]

    def __str__(self):
        return "{}".format(self.rect)

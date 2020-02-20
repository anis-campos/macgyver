from gui.images.sprite import Sprite
from gui.images.spritesheet import SpriteSheet
from gui.resource.tile_mapping import FLOOR_DEFAULT, FLOOR_START, FLOOR_END
from gui.tiles.floor_type import FloorType
from gui.tiles.tile import Tile


class Floor(Tile):
    _switcher = {
        FloorType.DEFAULT: FLOOR_DEFAULT,
        FloorType.START: FLOOR_START,
        FloorType.END: FLOOR_END,
    }

    def __init__(self, floor_type: FloorType = FloorType.DEFAULT):
        self.floor_type = floor_type
        super().__init__()

    @property
    def sprite_sheet(self) -> SpriteSheet:
        return self.loader.SHEET_FLOOR

    @property
    def sprite(self) -> Sprite:
        return self._switcher[self.floor_type]

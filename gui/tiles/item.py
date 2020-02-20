from enum import Enum

from gui.images.sprite import Sprite
from gui.images.spritesheet import SpriteSheet
from gui.resource.tile_mapping import NEEDLE, PLASTIC_PIPE, ETHER
from gui.tiles.tile_gui import TileGui
from model.labyrinth import Tile


class ItemType(Enum):
    NEEDLE = 1
    PLASTIC_PIPE = 2
    ETHER = 3


class Item(TileGui):

    def __init__(self, tile: Tile, item_type: ItemType):
        self.item_type = item_type
        super().__init__(tile)

    @property
    def sprite_sheet(self) -> SpriteSheet:
        if self.item_type == ItemType.NEEDLE:
            return self.loader.NEEDLE
        if self.item_type == ItemType.PLASTIC_PIPE:
            return self.loader.PLASTIC_PIPE
        elif self.item_type == ItemType.ETHER:
            return self.loader.ETHER

    @property
    def sprite(self) -> Sprite:
        if self.item_type == ItemType.NEEDLE:
            return NEEDLE
        if self.item_type == ItemType.PLASTIC_PIPE:
            return PLASTIC_PIPE
        elif self.item_type == ItemType.ETHER:
            return ETHER

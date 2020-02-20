from enum import Enum

from gui.images.sprite import Sprite
from gui.images.spritesheet import SpriteSheet
from gui.resource.tile_mapping import MACGYVER, GUARDIAN
from gui.tiles.tile_gui import TileGui
from model.labyrinth import Tile


class CharacterType(Enum):
    PLAYER = 1
    GUARDIAN = 2


class Character(TileGui):

    def __init__(self, tile: Tile, character_type: CharacterType):
        self.character_type = character_type
        super().__init__(tile)

    @property
    def sprite_sheet(self) -> SpriteSheet:
        if self.character_type == CharacterType.PLAYER:
            return self.loader.SHEET_PLAYER
        elif self.character_type == CharacterType.GUARDIAN:
            return self.loader.SHEET_GUARDIAN

    @property
    def sprite(self) -> Sprite:
        if self.character_type == CharacterType.PLAYER:
            return MACGYVER
        elif self.character_type == CharacterType.GUARDIAN:
            return GUARDIAN

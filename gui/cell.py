"""
Module for managing platforms.
"""
from enum import Enum

import pygame

from gui.constants import BLOCK_SIZE
from gui.loaders import ResourceLoader
from gui.sprite import Sprite
from gui.spritesheet import SpriteSheet

FLOOR_DEFAULT = Sprite(0, 40, 20, 20)
FLOOR_START = Sprite(16*20, 11*20, 20, 20)
FLOOR_END = Sprite(0, 0, 20, 20)
WALL_DEFAULT = Sprite(40, 140, 20, 20)


class Cell(pygame.sprite.Sprite):
    """ Cell of the maze """
    rect: pygame.Rect

    @property
    def sprite(self) -> Sprite:
        raise NotImplemented()

    @property
    def sprite_sheet(self) -> SpriteSheet:
        raise NotImplemented()

    def __init__(self):
        """ Cell constructor """
        super().__init__()

        self.loader = ResourceLoader()

        # Grab the image for this cell
        self.image = self.sprite_sheet.get_image(self.sprite.x,
                                                 self.sprite.y,
                                                 self.sprite.height,
                                                 self.sprite.width)
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.image.get_rect()


class FloorType(Enum):
    DEFAULT = 1
    START = 2
    END = 3


class Floor(Cell):
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


class WallType(Enum):
    DEFAULT = 1


class Wall(Cell):
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

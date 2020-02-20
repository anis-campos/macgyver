"""
Module for managing platforms.
"""

import pygame

from gui import BLOCK_SIZE
from gui.resource.loaders import ResourceLoader
from gui.images.sprite import Sprite
from gui.images.spritesheet import SpriteSheet


class Tile(pygame.sprite.Sprite):
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

        # Grab the image for this tiles
        self.image = self.sprite_sheet.get_image(self.sprite.x,
                                                 self.sprite.y,
                                                 self.sprite.height,
                                                 self.sprite.width)
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.image.get_rect()

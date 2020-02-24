"""
Module for managing platforms.
"""

import pygame

from gui import BLOCK_SIZE
from gui.images.sprite import Sprite
from gui.images.spritesheet import SpriteSheet
from gui.resource.loaders import ResourceLoader
from model.labyrinth import Tile


class TileGui(pygame.sprite.Sprite):
    """ Tile of the maze """
    tile: Tile
    rect: pygame.Rect

    @property
    def sprite(self) -> Sprite:
        raise NotImplemented()

    @property
    def sprite_sheet(self) -> SpriteSheet:
        raise NotImplemented()

    def __init__(self, tile: Tile):
        """ Tile constructor """
        super().__init__()
        
        self.tile = tile

        self.loader = ResourceLoader()

        # Grab the image for this tiles
        self.image = self.sprite_sheet.get_image_from_sprite(self.sprite)
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))

        #setting tile position
        self.rect = self.image.get_rect()
        self.rect.x = tile.x * BLOCK_SIZE
        self.rect.y = tile.y * BLOCK_SIZE

from typing import Set

import pygame

from gui import BLOCK_SIZE
from gui.tiles.character import Character, CharacterType
from gui.tiles.item import ItemType
from model.labyrinth import Tile


class Player(Character):
    items: Set[ItemType]
    rect: pygame.Rect

    def __init__(self, tile):
        super().__init__(tile, CharacterType.PLAYER)

        self.steps = 0
        self.items = set()
        self.change_y = 0
        self.change_x = 0

    def update(self):
        if self.change_y != 0 or self.change_x != 0:
            self.steps += 1
            self.rect.x += self.change_x
            self.rect.y += self.change_y
            self.tile = Tile(self.rect.x / BLOCK_SIZE, self.rect.y / BLOCK_SIZE)

    def go_left(self):
        self.change_x = -BLOCK_SIZE
        self.change_y = 0

    def go_right(self):
        self.change_x = BLOCK_SIZE
        self.change_y = 0

    def go_up(self):
        self.change_x = 0
        self.change_y = -BLOCK_SIZE

    def go_down(self):
        self.change_x = 0
        self.change_y = BLOCK_SIZE

    def stop(self):
        self.change_x = 0
        self.change_y = 0

    def take_item(self, item_type):
        self.items.add(item_type)

    def next_tile(self):
        rect = self.rect.copy()
        rect.x += self.change_x
        rect.y += self.change_y
        tile = Tile(rect.x / BLOCK_SIZE, rect.y / BLOCK_SIZE)
        return tile



import pygame
from termcolor import colored

from gui import BLOCK_SIZE
from gui.tiles.character import Character, CharacterType
from gui.tiles.wall import Wall
from model.labyrinth import Tile


class Player(Character):
    rect: pygame.Rect

    def __init__(self, tile):
        super().__init__(tile, CharacterType.PLAYER)

        self.items = set()
        self.change_y = 0
        self.change_x = 0

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.tile = Tile(self.rect.x / BLOCK_SIZE, self.rect.y/ BLOCK_SIZE)

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

    def hit_wall(self, wall: Wall):
        print(colored('player at {} hit wall at  {}'.format(self.rect, wall), 'red'))
        block = wall.rect
        if self.change_x > 0:
            self.rect.right = block.left
        elif self.change_x < 0:
            # Otherwise if we are moving left, do the opposite.
            self.rect.left = block.right
        if self.change_y > 0:
            self.rect.bottom = block.top
        elif self.change_y < 0:
            # Otherwise if we are moving left, do the opposite.
            self.rect.top = block.bottom
        self.tile = Tile(self.rect.x / BLOCK_SIZE, self.rect.y / BLOCK_SIZE)
        self.stop()

    def take_item(self, item_type):
        self.items.add(item_type)

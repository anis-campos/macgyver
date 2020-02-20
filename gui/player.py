import pygame

from gui import BLOCK_SIZE
from gui.resource.loaders import ResourceLoader
from gui.images.sprite import Sprite
from termcolor import colored

from gui.tiles.wall import Wall

MACGYVER = Sprite(0, 0, 43, 32)


class Player(pygame.sprite.Sprite):
    rect: pygame.Rect

    def __init__(self):
        super().__init__()

        self.loader = ResourceLoader()

        self.change_y = 0
        self.change_x = 0
        self.image = self.loader.SHEET_PLAYER.get_image_from_sprite(MACGYVER)
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

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
        print (colored('player at {} hit wall at  {}'.format(self.rect, wall,'red')))
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

        self.stop()

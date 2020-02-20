import random
from typing import List

import pygame

from gui.guardian import Guardian
from gui.level.level import Level
from gui.level.level01 import Level01
from gui.player import Player
from gui.tiles.item import Item, ItemType
from model.labyrinth import Tile


class Game:

    def __init__(self):
        # Set the current level
        self.current_level: Level = Level01()
        # Create the player
        self.player = Player(self.current_level.start.tile)
        self.guardian = Guardian(self.current_level.guardian)
        self.characters = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.item_tiles: List[Tile] = [tile_gui.tile for tile_gui in random.sample(self.current_level.floors, 3)]
        self.needle = Item(self.item_tiles[0], ItemType.NEEDLE)
        self.pipe = Item(self.item_tiles[1], ItemType.PLASTIC_PIPE)
        self.ether = Item(self.item_tiles[2], ItemType.ETHER)
        self.items.add(self.needle, self.pipe, self.ether)
        self.characters.add(self.guardian, self.player)
        # Loop until the user clicks the close button.
        self.done = False
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

    def collision_handler(self):
        block_hit_list = pygame.sprite.spritecollide(self.player, self.current_level.walls, False)
        if len(block_hit_list) > 0:
            self.player.hit_wall(block_hit_list[0])

    def end_game(self):
        if abs(self.player.tile.x - self.guardian.tile.x) + abs(self.player.tile.y - self.guardian.tile.y) == 1:
            print("game over")

    def item_detection(self):
        block_hit_list: List[Item] = pygame.sprite.spritecollide(self.player, self.items, False)
        for block in block_hit_list:
            self.player.take_item(block.item_type)
            self.items.remove(block)
            print('On item {}'.format(block.item_type))

    def out_of_game(self):
        if self.player.change_x > 0 and self.player.tile.x == self.current_level.width - 1 \
                or self.player.change_x < 0 and self.player.tile.x == 0 \
                or self.player.change_y < 0 and self.player.tile.x == 0 \
                or self.player.change_y > 0 and self.player.tile.y == self.current_level.height - 1:
            self.player.stop()
            print('trying to get out of game')

    def game_loop(self, screen):

        # -------- Main Program Loop -----------
        while not self.done:
            pygame.time.delay(100)
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True  # Flag that we are done so we exit this loop
                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                        self.player.stop()

            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[pygame.K_LEFT]:
                self.player.go_left()
            if pressed_keys[pygame.K_RIGHT]:
                self.player.go_right()
            if pressed_keys[pygame.K_UP]:
                self.player.go_up()
            if pressed_keys[pygame.K_DOWN]:
                self.player.go_down()

            self.out_of_game()

            self.characters.update()
            self.current_level.update()

            self.end_game()

            self.item_detection()

            self.collision_handler()

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            self.current_level.draw(screen)
            self.items.draw(screen)
            self.characters.draw(screen)

            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

            # Limit to 60 frames per second
            self.clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

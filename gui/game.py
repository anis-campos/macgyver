import random
from typing import List

import pygame

from gui import SCREEN_HEIGHT, SCREEN_WIDTH
from gui.guardian import Guardian
from gui.level.level import Level
from gui.level.level01 import Level01
from gui.player import Player
from gui.tiles.item import Item, ItemType
from gui.window_specific import window_on_top
from model.labyrinth import Tile


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    window_on_top(pygame.display.get_wm_info()['window'])

    pygame.display.set_caption("Platformer with sprite sheets")

    # Set the current level
    current_level: Level = Level01()

    # Create the player
    player = Player(current_level.start.tile)

    guardian = Guardian(current_level.guardian)

    active_sprite_list = pygame.sprite.Group()
    items = pygame.sprite.Group()

    item_tiles: List[Tile] = [tile_gui.tile for tile_gui in random.sample(current_level.floors,3)]

    needle = Item(item_tiles[0], ItemType.NEEDLE)
    pipe = Item(item_tiles[1], ItemType.PLASTIC_PIPE)
    ether = Item(item_tiles[2], ItemType.ETHER)

    items.add(needle, pipe, ether)

    active_sprite_list.add(player, guardian)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        pygame.time.delay(100)
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    player.stop()

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            player.go_left()
        if pressed_keys[pygame.K_RIGHT]:
            player.go_right()
        if pressed_keys[pygame.K_UP]:
            player.go_up()
        if pressed_keys[pygame.K_DOWN]:
            player.go_down()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        collision_handler(current_level, player)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        items.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


def collision_handler(current_level, player):
    block_hit_list = pygame.sprite.spritecollide(player, current_level.walls, False)
    if len(block_hit_list) > 0:
        player.hit_wall(block_hit_list[0])


if __name__ == "__main__":
    main()

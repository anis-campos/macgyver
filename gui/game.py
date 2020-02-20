from ctypes import windll, Structure, c_long, byref  # windows only

import pygame

from gui import SCREEN_HEIGHT, SCREEN_WIDTH
from gui.level.level01 import Level01
from gui.player import Player


class RECT(Structure):
    _fields_ = [
        ('left', c_long),
        ('top', c_long),
        ('right', c_long),
        ('bottom', c_long),
    ]

    def width(self):  return self.right - self.left

    def height(self): return self.bottom - self.top


def onTop(window):
    SetWindowPos = windll.user32.SetWindowPos
    GetWindowRect = windll.user32.GetWindowRect
    rc = RECT()
    GetWindowRect(window, byref(rc))
    SetWindowPos(window, -1, rc.left, rc.top, 0, 0, 0x0001)


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    onTop(pygame.display.get_wm_info()['window'])

    pygame.display.set_caption("Platformer with sprite sheets")

    # Create the player
    player = Player()

    # Set the current level
    current_level = Level01()

    active_sprite_list = pygame.sprite.Group()

    player.rect = current_level.start.rect.copy()

    active_sprite_list.add(player)

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

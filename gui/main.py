import pygame

from gui import SCREEN_HEIGHT, SCREEN_WIDTH
from gui.game import Game
from gui.window_specific import window_on_top


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    window_on_top(pygame.display.get_wm_info()['window'])

    pygame.display.set_caption("Platformer with sprite sheets")

    game = Game()
    game.game_loop(screen)

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()

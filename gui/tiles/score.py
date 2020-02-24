import pygame

from gui import WHITE, BLOCK_SIZE, BLACK
from gui.game_state import GameState
from gui.player import Player


class Score(pygame.sprite.Sprite):
    def __init__(self, player: Player, width, height):
        super().__init__()
        self._player = player
        self.image = pygame.Surface((width, BLOCK_SIZE * 7))
        self.rect = self.image.get_rect()
        self.rect.y = height

    font_name = pygame.font.match_font('arial')

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect: pygame.Rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.image.blit(text_surface, text_rect)

    def update(self, state: GameState):
        self.image.fill(BLACK)
        self.draw_text('Player Score:', 26, 10, 10)
        if len(self._player.items) < 3:
            items = [item.name for item in self._player.items]
            self.draw_text('Items : {}'.format(items), 18, 15, 45)
        else:
            self.draw_text('Items : {}'.format('WEAPON'), 18, 15, 45)
        self.draw_text('Steps : {}'.format(self._player.steps), 18, 15, 65)

        if len(self._player.items) == 0:
            self.draw_text('MacGyver need you help !', 20, 200, 50)
            self.draw_text('Find the 3 pieces of the tool and take down the guardian !', 20, 200, 70)

        if state == GameState.HAVE_WEAPON:
            self.draw_text('You have a weapon', 20, 200, 50)
            self.draw_text('YOu can take down the guardian!', 20, 200, 70)

        if state == GameState.GUARDIAN_DOWN:
            self.draw_text('The guardian is down', 20, 200, 50)
            self.draw_text('YOu can escape!', 20, 200, 70)
# Todo : add to the score :
# - Time

import pygame

from gui import WHITE


class GameOver(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((width,height))
        self.rect = self.image.get_rect()
        self.draw_text('GAME OVER!', 50, width/2, height/2)

    font_name = pygame.font.match_font('arial')

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect: pygame.Rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.image.blit(text_surface, text_rect)


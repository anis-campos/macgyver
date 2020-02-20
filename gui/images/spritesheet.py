import pygame

from gui import BLACK
from gui.images.sprite import Sprite


class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name, color=BLACK):
        """ Constructor. Pass in the file name of the sprite sheet.
        :param color: Transparency color, assuming black
        :type color: object
        """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

        self.color = color

    def get_image_from_sprite(self, sprite: Sprite) -> pygame.Surface:
        return self.get_image(sprite.x, sprite.y, sprite.width, sprite.height)

    def get_image(self, x, y, width, height) -> pygame.Surface:
        """ Grab a single image out of a larger sprite sheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # set transparent color
        image.set_colorkey(self.color)

        # Return the image
        return image

import pygame

from gui.tiles.character import Character, CharacterType


class Guardian(Character):

    def __init__(self, tile):
        super().__init__(tile, CharacterType.GUARDIAN)

from Singleton import Singleton
from gui.resource import *
from gui.images.spritesheet import SpriteSheet


class ResourceLoader(metaclass=Singleton):
    SHEET_PLAYER: SpriteSheet
    SHEET_FLOOR: SpriteSheet
    SHEET_WALL: SpriteSheet

    def __init__(self):
        self.SHEET_PLAYER = SpriteSheet(SHEET_PLAYER_PATH)
        self.SHEET_FLOOR = SpriteSheet(SHEET_FLOOR_PATH)
        self.SHEET_WALL = SpriteSheet(SHEET_WALL_PATH)

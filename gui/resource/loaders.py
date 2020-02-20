from common.Singleton import Singleton
from gui.images.spritesheet import SpriteSheet
from gui.resource import *


class ResourceLoader(metaclass=Singleton):
    SHEET_PLAYER: SpriteSheet
    SHEET_FLOOR: SpriteSheet
    SHEET_WALL: SpriteSheet

    def __init__(self):
        self.SHEET_PLAYER = SpriteSheet(SHEET_PLAYER_PATH)
        self.SHEET_GUARDIAN = SpriteSheet(SHEET_GUARDIAN_PATH)
        self.SHEET_FLOOR = SpriteSheet(SHEET_FLOOR_PATH)
        self.SHEET_WALL = SpriteSheet(SHEET_WALL_PATH)

import os

from common.Singleton import Singleton
from gui.images.spritesheet import SpriteSheet
from conf import ROOT_DIR

SHEET_PLAYER_PATH = os.path.join(ROOT_DIR, 'resources', 'sprites', 'MacGyver.png')
SHEET_GUARDIAN_PATH = os.path.join(ROOT_DIR, 'resources', 'sprites', 'Gardien.png')
SHEET_FLOOR_PATH = os.path.join(ROOT_DIR, 'resources', 'sprites', 'floor-tiles-20x20.png')
SHEET_WALL_PATH = os.path.join(ROOT_DIR, 'resources', 'sprites', 'structures.png')

SHEET_NEEDLE_PATH = os.path.join(ROOT_DIR, 'resources', 'sprites', 'aiguille.png')
SHEET_PLASTIC_PIPE_PATH = os.path.join(ROOT_DIR, 'resources', 'sprites', 'tube_plastique.png')
SHEET_ETHER_PATH = os.path.join(ROOT_DIR, 'resources', 'sprites', 'ether.png')


class ResourceLoader(metaclass=Singleton):
    SHEET_PLAYER: SpriteSheet
    SHEET_FLOOR: SpriteSheet
    SHEET_WALL: SpriteSheet
    NEEDLE: SpriteSheet
    PLASTIC_PIPE: SpriteSheet
    ETHER: SpriteSheet

    def __init__(self):
        self.SHEET_PLAYER = SpriteSheet(SHEET_PLAYER_PATH)
        self.SHEET_GUARDIAN = SpriteSheet(SHEET_GUARDIAN_PATH)

        self.SHEET_FLOOR = SpriteSheet(SHEET_FLOOR_PATH)
        self.SHEET_WALL = SpriteSheet(SHEET_WALL_PATH)

        self.NEEDLE = SpriteSheet(SHEET_NEEDLE_PATH)
        self.PLASTIC_PIPE = SpriteSheet(SHEET_PLASTIC_PIPE_PATH)
        self.ETHER = SpriteSheet(SHEET_ETHER_PATH)

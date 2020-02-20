from gui import BLOCK_SIZE
from gui.images.sprite import Sprite

FLOOR_DEFAULT = Sprite(0, 40, 20, 20)
FLOOR_START = Sprite(16 * BLOCK_SIZE, 11 * BLOCK_SIZE, 20, 20)
FLOOR_END = Sprite(0, 0, 20, 20)
WALL_DEFAULT = Sprite(40, 140, 20, 20)

MACGYVER = Sprite(0, 0, 32, 43)
GUARDIAN = Sprite(0, 0, 32, 36)
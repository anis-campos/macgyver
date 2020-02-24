from enum import Enum


class GameState(Enum):
    LOOKING_FOR_ITEMS = 1
    HAVE_WEAPON = 2
    GUARDIAN_DOWN = 3
    LOOSE = 4
    WIN = 5
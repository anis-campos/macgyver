from gui.spritesheet import SpriteSheet


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ResourceLoader(metaclass=Singleton):
    SHEET_PLAYER: SpriteSheet
    SHEET_FLOOR: SpriteSheet
    SHEET_WALL: SpriteSheet

    def __init__(self):
        self.SHEET_PLAYER = SpriteSheet('../sprites/MacGyver.png')
        self.SHEET_FLOOR = SpriteSheet('../sprites/floor-tiles-20x20.png')
        self.SHEET_WALL = SpriteSheet('../sprites/structures.png')

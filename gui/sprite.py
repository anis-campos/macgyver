class Sprite:
    def __init__(self, x: int, y: int, height: int, width: int):
        """
        :param x: x position corner top right
        :param y: y position corner top right
        :param height: height of sprite
        :param width: width of the sprite
        """
        self.width = width
        self.height = height
        self.y = y
        self.x = x

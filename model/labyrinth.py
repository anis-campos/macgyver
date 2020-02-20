import enum


class TileType(enum.Enum):
    """
    Enum representing type of tiles
    """
    WALL = 1
    HALL = 2
    START = 3
    END = 4


class Tile:

    def __init__(self, x=0, y=0, tile_type=None):
        self.x = x
        self.y = y
        self.type = tile_type


class Labyrinth:

    def __init__(self, nb_row=0, nb_col=0, maze=None, start=None, end=None):
        """

        :param nb_row:
        :type nb_row: int
        :param nb_col: int
        :param maze: Map of the labyrinth
        :type maze: list of Tile
        :param start: Begin position of player
        :type start: Tile
        :param end: End game position
        :type end: Tile
        """
        self.nb_row = nb_row
        self.nb_col = nb_col
        self.mazeMap = maze
        self.start = start
        self.end = end

    @staticmethod
    def parse(char):
        """
        This method is used to parse the string representation of a level
        :param char:
        :return:
        """
        if char == ' ':
            return TileType.HALL
        elif char == '#':
            return TileType.WALL
        elif char == 'A':
            return TileType.START
        elif char == "B":
            return TileType.END
        else:
            raise Exception("Unknown tiles type")

    def load(self, file_name: str):
        with open(file_name) as f:
            content = f.read().splitlines()
        self.nb_row = len(content)
        self.nb_col = len(content[0])
        self.mazeMap = [Tile(x=j, y=i, tile_type=self.parse(col)) for i, line in enumerate(content) for j, col in
                        enumerate(line)]
        self.start = [a for a in self.mazeMap if a.type == TileType.START].pop()
        self.end = [a for a in self.mazeMap if a.type == TileType.END].pop()

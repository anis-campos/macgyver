import unittest
from labyrinth import Labyrinth


class LabyrinthTestCase(unittest.TestCase):
    def test_can_load_file(self):
        labyrinth = Labyrinth()
        labyrinth.load('./level_1')
        assert len(labyrinth.mazeMap) > 0
        assert labyrinth.nb_col == 37
        assert labyrinth.nb_row == 23
        assert labyrinth.start.x == 22
        assert labyrinth.start.y == 1
        assert labyrinth.end.x == 0
        assert labyrinth.end.y == 35


if __name__ == '__main__':
    unittest.main()

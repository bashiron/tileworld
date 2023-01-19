from unittest import TestCase
from unittest.mock import patch, Mock, MagicMock

from game import Grid, Coord

class TestGrid(TestCase):

    def test_init(self):
        grid1 = Grid(8, 8)
        grid1.get_tile(Coord(4, 4))
        pass


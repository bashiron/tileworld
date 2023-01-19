from unittest import TestCase
from unittest.mock import patch, Mock, MagicMock

import grid
import tile

class TestGrid(TestCase):

    def test_init(self):
        grid1 = grid.Grid(8, 8)
        grid1.get_tile(grid.Coord(4, 4))
        pass


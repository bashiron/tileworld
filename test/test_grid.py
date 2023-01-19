from unittest import TestCase
from unittest.mock import patch, Mock, MagicMock

from game import *
from instances.consumables import estus
class TestGrid(TestCase):

    def test_init(self):
        grid1 = Grid(8, 8)
        assert grid1.get_tile(Coord(4, 4)).load == []

    def test_tile_coord(self):
        """Test if the Tiles were created with the appropiate coordinates."""
        grid1 = Grid(8, 8)
        coord1 = Coord(7, 2)
        assert grid1.get_tile(coord1).coord == coord1

    def test_populate(self):
        """Test grid method for populating its tiles with random content"""
        grid1 = Grid(8, 8)
        grid1.populate()
        arb_tile = grid1.get_tile(Coord(3, 6))  # arbitrary tile
        self.assertLessEqual(density[0], len(arb_tile.load))
        self.assertGreaterEqual(density[1], len(arb_tile.load))

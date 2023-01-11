from world import World

from unittest import TestCase

class TestWorld(TestCase):

    def test_empty(self):
        world = World(5, 5)
        # pick random tile and check for emptiness
        assert world.tiles[2][2].load == []

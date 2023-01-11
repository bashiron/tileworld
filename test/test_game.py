from game import Game
from player import Player
from world import World
from weapon import Weapon

from unittest import TestCase

class TestGame(TestCase):

    def test_idle(self):
        p_bashiron = Player('Bashiron')
        w_lordran = World()
        game = Game(p_bashiron, w_lordran)
        game.tick()
        assert True

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

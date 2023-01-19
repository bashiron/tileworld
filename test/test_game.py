from unittest import TestCase

from game import *

class TestGame(TestCase):

    def test_idle(self):
        p_bashiron = Player('Bashiron')
        g_lordran = Grid(10, 10)
        game = Game(p_bashiron, g_lordran)
        game.tick()
        assert True

    def test_something(self):
        p_bashiron = Player('Bashiron')
        p_bashiron.greet()
        p_bashiron.lol()

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

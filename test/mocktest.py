import world

from unittest.mock import patch
from unittest import TestCase

class TestMock(TestCase):

    @patch('world.World')
    def test_type(self, MockWorld):
        world.World(10, 20)
        assert MockWorld is world.World
        assert MockWorld.called


# example of patch with no with or decorator
# Original = Class
# patcher = patch('__main__.Class', spec=True)
# MockClass = patcher.start()
# instance = MockClass()
# assert isinstance(instance, Original)
# patcher.stop()

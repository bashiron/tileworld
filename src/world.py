from tile import Tile
from numpy import full

class World:
    """Game world. Contains the physical "map" (grid of tiles) as well as other variables like weather or
     """

    def __init__(self, x, y):
        # TODO at this point i should probably instantiate each tile with its coordinate (as tuple) as a class attribute
        # TODO maybe i could first create a normal (x y) matrix or use a sequence instead of just Tile()
        self.tiles = full((x, y), Tile())
        self.weather = None

    def tick(self):
        pass

from functools import reduce
from physical import Physical
from grid import Coord


class Tile:
    """Minimal atomic space in the game `World`.
    """

    load: list[Physical]
    """Stuff inhabiting the tile.
    """

    coord: Coord
    """Tile position in the grid.
    """

    def __init__(self, coord, load=None):
        self.load = load if load is not None else []    # stuff inhabiting the tile
        self.coord = coord

    # TODO do i need getters?
    def get_load(self):
        return self.load

    def __str__(self):
        return reduce(lambda x, y: str(x) + ', ' + str(y), self.load)

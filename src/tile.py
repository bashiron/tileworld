from functools import reduce


class Tile:
    """Minimal atomic space in the game `World`.

    Parameters
    -----
    load : `list` of `physical.Physical`
        Stuff inhabiting the tile.
    """

    def __init__(self, load=None):
        self.load = load if load is not None else []    # stuff inhabiting the tile

    def __str__(self):
        return reduce(lambda x, y: str(x) + ', ' + str(y), self.load)

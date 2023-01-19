import tile

from collections.abc import Callable
from more_itertools import map_if

class Coord:
    """2D coordinate inside the Grid.
    """

    x: int
    """X axis.
    """

    y: int
    """Y axis.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Grid:
    """World grid, two dimensional structure composed of Tiles.
    """

    matrix: list[list[tile.Tile]]
    """2D structure that contains the Tiles.
    """

    def __init__(self, width, height):
        self.matrix = [build_row(width, n) for n in range(height)]

    def get_tile(self, coord):
        """Fetch Tile at the given coordinates.

        Parameters
        -----
        coord : `Coord`
            Coordinate where Tile will be fetched.
        """
        return self.matrix[coord.y][coord.x]

    def retrieve(self, pred: Callable[[tile.Tile], bool]):
        """Return list of every Tile matching predicate conditions.

        Parameters
        -----
        pred
            Predicate to check on Tiles.

        Returns
        -----
        `list` of `Tile`
            Tiles that satisfy the predicate.
        """
        res = []
        for row in self.matrix:
            # compile iterator where matching Tiles are themselves and non-matching Tiles are None, then filter out Nones
            row_res = list(filter(lambda x: x is not None, map_if(row, pred, lambda x: x, lambda x: None)))
            # alternative: get indexes of matching Tiles and then grab the Tiles using the indexes
            # row_res = [row[i] for i in locate(row, pred)]
            res.extend(row_res)
        return res

    def locate(self, pred: Callable[[tile.Tile], bool]):
        """Return list of coordinates of every Tile matching predicate conditions.

        Parameters
        -----
        pred
            Predicate to check on Tiles.

        Returns
        -----
        `list` of `Coord`
            Coords of Tiles that satisfy the predicate.
        """
        return [tile.coord for tile in self.retrieve(pred)]

    def retrieve_near(self, char, pred: Callable[[tile.Tile], bool]):
        """Return Tile matching predicate conditions that is closest to the player character.
        """
        # examine Tiles in a spiral iteration starting around player, break execution at first match
        pass

    def locate_near(self, char, pred: Callable[[tile.Tile], bool]):
        """Return coordinate of Tile matching predicate conditions that is closest to the player character.
        """
        # call locate_near() and take coords from resulting Tile
        pass

    def move_char(self, char, direc):
        """Move the character in the specified direction.
        """
        # when a character moves (any of 4 directions) their coord attribute should change and also the Grid has to
        # remove it from the previous Tile's "load" and put it in the new Tile's "load"
        pass

    def surroundings(self, char):
        """Return what is contained in the four (non-diagonally) adjacent Tiles.
        """
        # return a 4-value tuple with the load of tile in each direction
        # or return a dictionary where keys are the cardinal points and values their loads
        pass

def build_row(length, pos):
    from tile import Tile
    """Build a row of the specified length.

    Parameters
    -----
    length : `int`
        Length for the row.
    pos : `int`
        Row's position in the Y axis of the matrix. Used for instantiating the Tiles.

    Returns
    -----
    `list` of `Tile`
        Row with Tiles.
    """
    return [Tile(Coord(n, pos)) for n in range(length)]

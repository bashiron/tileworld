from tile import Tile

from collections.abc import Callable

class Coord:

    x: int
    """X axis.
    """

    y: int
    """Y axis.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Grid:
    """World grid, two dimensional structure composed of Tiles.
    """

    matrix: list[list[Tile]]
    """Low level structure that contains the Tiles.
    """

    def __init__(self, width, height):
        self.matrix = [build_row(width) for _ in range(height)]

    def get_tile(self, coord):
        """Fetch Tile at the given coordinates.
        """
        return self.matrix[coord.get_y()][coord.get_x()]

    def locate(self, pred: Callable[[Tile], bool]):
        """Return list of every Tile matching predicate conditions.
        """
        pass

    def space_locate(self, pred: Callable[[Tile], bool]):
        """Return list of coordinates of every Tile matching predicate conditions.
        """
        # call locate() and take coords from resulting Tiles
        pass

    def locate_near(self, char, pred: Callable[[Tile], bool]):
        """Return Tile matching predicate conditions that is closest to the player character.
        """
        # examine Tiles in a spiral iteration starting around player, break execution at first match
        pass

    def space_locate_near(self, char, pred: Callable[[Tile], bool]):
        """Return coordinate of Tile matching predicate conditions that is closest to the player character.
        """
        # call locate_near() and take coords from resulting Tile
        pass

    def move_char(self, char, direc):
        """Move the character in the specified direction.
        """
        pass

    def surroundings(self, char):
        """Return what is contained in the four (non-diagonally) adjacent Tiles.
        """
        # return a 4-value tuple with the load of tile in each direction
        # or return a dictionary where keys are the cardinal points and values their loads
        pass

def build_row(length):
    # TODO give coords to created Tile
    return [Tile(Coord()) for _ in range(length)]

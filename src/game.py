from abc import ABC
from collections.abc import Callable
from zope.interface import implementer, Interface, Attribute
from functools import reduce
from more_itertools import map_if

density = (0, 4)   # defines min and max amount of Items per Tile in the Grid

class Game:
    """Manager of the topmost game mechanics and execution flow.
    """
    def __init__(self, player, world):
        self.player = player
        self.world = world
        self.tick = 0

    def tick(self):
        self.world.tick()


class Physical(Interface):
    """Thing that takes up space in a `Tile`, has physical space.
    """

    def greet():
        print('im physical!')


@implementer(Physical)
class Item(ABC):
    """Abstract class representing items. Items have the property of being able to be possesed by a player.
    """

    name: str
    """Name."""
    weight: int
    """Weight."""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Weapon(Item):
    """Reusable item with the main purpose of dealing HP damage.
    """

    dmg: dict
    """Damage done by weapon."""
    crit: int
    """Critical chance % out of 100."""
    max_cond: int
    """Total, maximum and starting condition."""
    cond: int
    """Current condition."""

    def __init__(self, name, dmg, crit, cond, weight):
        super().__init__(name, weight)
        self.dmg = dmg
        self.crit = crit
        self.max_cond = cond
        self.cond = self.max_cond


class Inventory:
    """Item container attached to Player.
    """

    items: list[Item]
    """Inventory contents."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)


@implementer(Physical)
class Player:

    name: str
    """Player name."""
    hp: int
    """Health points."""
    sp: int
    """Stamina points."""
    weapon: Weapon
    """Currently equipped weapon."""
    inv: Inventory
    """Inventory, contains items."""

    def __init__(self, name):
        from instances.weapons import unarmed
        self.name = name
        self.hp = 100   # health points
        self.sp = 100   # stamina points
        self.weapon = unarmed
        self.inv = Inventory()

    def tick(self):
        pass

    def attack(self, enemy):
        pass

    def pick_up(self):
        pass

    def drop(self, item):
        """Drop item to the ground.
        """
        # remove item from inventory
        # add it to current Tile's load
        pass


class Enemy:

    name: str
    """Name."""
    hp: int
    """Health points."""
    dmg: dict
    """Damage done by enemy."""
    drops: list[Item]
    """Items dropped on enemy defeat."""

    def __init__(self, name, hp, dmg, drops):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.drops = drops


class Consumable(Item):
    """One-use item that causes an effect on Player and/or Enemy.
    """

    p_effect: Callable[[Player], None]
    """Effect on Player on use."""
    e_effect: Callable[[Enemy], None]
    """Effect on Enemy on use."""

    def __init__(self, name, p_effect, e_effect, weight):
        super().__init__(name, weight)
        self.p_effect = p_effect
        self.e_effect = e_effect


class Trait:
    """Bonuses for a character, a specialization
    """

    def __init__(self):
        pass


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

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

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

    def __str__(self):
        return reduce(lambda x, y: str(x) + ', ' + str(y), self.load)


class Grid:
    """World grid, two dimensional structure composed of Tiles.
    """

    matrix: list[list[Tile]]
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

    def retrieve(self, pred: Callable[[Tile], bool]):
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

    def locate(self, pred: Callable[[Tile], bool]):
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

    def retrieve_near(self, char, pred: Callable[[Tile], bool]):
        """Return Tile matching predicate conditions that is closest to the player character.
        """
        # examine Tiles in a spiral iteration starting around player, break execution at first match
        pass

    def locate_near(self, char, pred: Callable[[Tile], bool]):
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

    def populate(self):
        from utils import take_rand
        from instances.weapons import export as wps
        from instances.consumables import export as cons

        for tile in self.navigate():
            stuff = take_rand(wps + cons, density[0], density[1])
            tile.load.extend(stuff)

    def navigate(self):
        for row in self.matrix:
            for tile in row:
                yield tile


def build_row(length, pos):
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

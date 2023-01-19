from game import Consumable
from .misc import inert


def heal(player):
    player.hp += 40


estus = Consumable('Estus', heal, inert, 8)

# -----------------------------------------
export = [estus]

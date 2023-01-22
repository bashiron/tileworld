from game import Consumable, Player
from .misc import inert


def heal(player):
    player.hp += 40

def lesser_heal(player):
    player.hp += 20

def magic_hurt(enemy):
    enemy.hp -= 60

def phys_hurt(entity):
    if isinstance(entity, Player):
        entity.hp -= 20
    else:
        entity.hp -= 50

def staminup(player):
    player.sp += 60


# do not export
estus = Consumable('Estus', heal, inert, 8)

red_gem = Consumable('Red Gem', lesser_heal, inert, 4)

magic_bomb = Consumable('Magic Bomb', inert, magic_hurt, 10)

thorn_blast = Consumable('Thorn Blast', phys_hurt, phys_hurt, 10)

green_leaf = Consumable('Green Leaf', staminup, inert, 4)

# -----------------------------------------
export = [red_gem, magic_bomb, thorn_blast, green_leaf]

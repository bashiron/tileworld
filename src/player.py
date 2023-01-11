from weapon import Weapon
from physical import Physical

from zope.interface import implementer

@implementer(Physical)
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100   # health points
        self.sp = 100   # stamina points
        self.weapon = Weapon(
            'Unarmed',
            {
                'phys': 10,
                'magc': 0,
                'lgtn': 0,
                'fire': 0
            },
            999,
            15)

    def tick(self):
        pass

    def attack(self, enemy):
        pass

    def pick_up(self):
        pass

from player import Player
from world import World

class Game:
    def __init__(self, player, world):
        self.player = player
        self.world = world
        self.tick = 0

    def tick(self):
        self.world.tick()

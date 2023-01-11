class Weapon:

    def __init__(self, name, dmg, crit, cond):
        self.dmg = dmg    # damage values
        self.crit = crit    # critical chance % out of 100
        self.init_cond = cond   # total condition
        self.cond = self.init_cond  # current condition


from races.master import Race

class Mensch(Race):
    def __init__(self):
        super().__init__()
        self.boni["ST"] = 5
        self.boni["SD"] = 5
from races.master import Race

class Mensch(Race):
    def __init__(self):
        super().__init__()
        self.boni["ST"] = 10
        self.boni["QU"] = -5
        self.boni["PR"] = 10
        self.boni["CO"] = 10
        self.boni["AG"] = -5

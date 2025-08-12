from races.master import Race

class Zwerg(Race):
    def __init__(self):
        super().__init__()
        self.boni["ST"] = 5
        self.boni["CO"] = 15
        self.boni["SD"] = 5
        self.boni["PR"] = -10
        self.boni["QU"] = -5
        self.boni["EM"] = -10
        self.boni["AG"] = -5
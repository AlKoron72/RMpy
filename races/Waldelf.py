from races.master import Race

class Waldelf(Race):
    def __init__(self):
        super().__init__()
        self.boni["QU"] = 10
        self.boni["PR"] = 10
        self.boni["ME"] = 5
        self.boni["EM"] = 5
        self.boni["AG"] = 5
        self.boni["SD"] = -20
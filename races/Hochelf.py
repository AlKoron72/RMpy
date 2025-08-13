from races.master import Race

class Hochelf(Race):
    def __init__(self):
        super().__init__()
        self.boni["QU"] = 10
        self.boni["PR"] = 10
        self.boni["ME"] = 5
        self.boni["EM"] = 5
        self.boni["AG"] = 5
        self.boni["SD"] = -20
        self.resistance["essence", "mentalism", "channeling"] = -5
        self.resistance["poison"] = 10
        self.resistance["diseases"] = 100
        self.soul_departure_rd = 2
        self.hp_dice = 8
        self.recovery = 2.0
from races.master import Race

class Mensch(Race):
    def __init__(self):
        super().__init__()
        self.boni["ST"] = 10
        self.boni["QU"] = -5
        self.boni["PR"] = 10
        self.boni["CO"] = 10
        self.boni["AG"] = -5
        self.slot_name = "Hoher Mensch (altes Volk)"
        self.soul_departure_rd = 10
        self.languages_nr = 3
        self.resistances["essence", "mentalism"] = -5
        self.resistances["channeling"] = 5
        self.recovery = 0.7

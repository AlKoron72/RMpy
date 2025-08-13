from races.master import Race

class Mensch(Race):
    def __init__(self):
        super().__init__()
        self.boni["ST"] = 5
        self.boni["SD"] = 5
        self.language_nr = 2
        self.slot_name = "Mensch (gewöhnlicher)"
        self.hp_dice = 8
        self.soul_departure_rd = 12
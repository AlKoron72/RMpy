from SHORTS import SHORTS

class Race:
    def __init__(self, name:str = "", **args):
        self.name = name
        self.slot_name = "Mensch (gewöhnlich)" # ein Beschreibungstext für die Dropdowns
        self.boni = {}
        self.hp_dice = 10
        self.languages_nr = 1
        self.recovery = 1.0
        self.soul_departure_rd = 1
        self.resistances = {
            "poison": 0,
            "disease": 0,
            "essence": 0,
            "mentalism": 0,
            "channeling": 0,
        }
        for s in SHORTS:
            self.boni[s.name] = 0
        
    def __str__(self) -> str:
        return_value = "Boni für:\n"
        for key, value in self.boni.items():
            return_value += f"{key}: {value}\n"
        for key, value in self.resistances.items():
            return_value += f"{key}: {value}\n"
        return_value += f"Recovery-Multiplier: {self.recovery}\n"
        return_value += f"HP-Dice: D{self.hp_dice}\n"
        return_value += f"Number of starting Languages: {self.languages_nr}\n"
        return return_value
    
if __name__ == "__main__":
    # Example usage
    racing = Race()
    print(racing)

import Bonus
import SHORTS
from Rolls import Rolls
from tables import max_stats

def get_bonus(for_value:int) -> int:
    bonus = Bonus.standard_bonus(for_value)
    return bonus

class Stat:
    # standardShorts = ("ST", "QU", "PR", "IN", "EM", "SD", "RE", "ME", "CO", "AG")

    def __init__(self, name:str, value:int):
        self.name = name
        self.value = value
        self.max_value = 0
        self.bonus = get_bonus(self.value)
        self.bonus_race = 0
        self.total = self.bonus + self.bonus_race

    def __str__(self):
        to_string = f"Abbreviation: {self.name}\n"
        to_string += f"Value:        {self.value}\n"
        to_string += f"Max-Value:    {self.max_value}\n"
        to_string += f"Bonus:        {self.bonus}\n"
        to_string += f"Bonus-Race:   {self.bonus_race}\n"
        to_string += f"Total bonus:  {self.total}\n"
        to_string += f"Bonus:        {self.bonus}\n"
        return to_string
    
    def set_max_value(self, value:int) -> int:
        return_value = value
        
        # init Rolls-Class and uses it to roll
        roller = Rolls(100)
        roll_max = roller.roll()
        if roll_max > value:
            self.max_value = roll_max
        else:
            self.max_value = value
        # uses the roll, to look up in table and return the max-Value (pot. Value)
        # return max_stats.return_max_simple(value, roll_max)
        return return_value

    def update_max_value(self, value:int) -> int:
        return_value = value
        return return_value

if __name__ == "__main__":
    # Example usage
    myValue = Rolls(100).roll()
    test = Stat("ST", myValue)
    print(test)

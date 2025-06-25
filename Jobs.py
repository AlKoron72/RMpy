import Bonus
import SHORTS
from Rolls import Rolls

class Jobs:
    # standardShorts = ("ST", "QU", "PR", "IN", "EM", "SD", "RE", "ME", "CO", "AG")

    def __init__(self, name:str = None, value:int = 0):
        self.name = name
        self.value = value

    def __str__(self):
        to_string = f"Abbreviation: {self.name}\n"
        to_string += f"Value:        {self.value}\n"

        return to_string

if __name__ == "__main__":
    # Example usage
    myValue = Rolls(100).roll()
    test = Jobs("ST", myValue)
    print(test)

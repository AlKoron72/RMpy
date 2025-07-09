import Bonus
import SHORTS
from Rolls import Rolls

class Dieb:
    # standardShorts = ("ST", "QU", "PR", "IN", "EM", "SD", "RE", "ME", "CO", "AG")

    def get_prime(self, job_str:str) -> str:
        shorts_list = ["QU", "AG"]
        return shorts_list
    
    def __init__(self, name:str):
        self.name = name
        self.prime_stats = self.get_prime(name)

    def __str__(self) -> str:
        to_string = f"Job:              {self.name}\n"
        to_string += f"Prime-Stats:      {self.prime_stats}\n"
        return to_string

if __name__ == "__main__":
    # Example usage
    #myValue = Rolls(100).roll()
    test = Dieb("Dieb")
    print(test)

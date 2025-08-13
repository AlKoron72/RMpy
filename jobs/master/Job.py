"""
this is a master class for all Jobs
the jobs get extended by all Job-Classes in folder jobs
main functions get provided by this class
---
made by: Alexander Günther
date: 08/2025
"""


class Job:
    # SHORTS = ("ST", "QU", "PR", "IN", "EM", "SD", "RE", "ME", "CO", "AG")

    def __init__(self, name: str):
        self.name = name
        self.prime_stats = self.get_prime()
        self.spell_stat = None  # Default: kein Spell-Attribut

    def get_spell_stat(self) -> str:
        return self.spell_stat

    def get_prime(self) -> list[str]:
        # Default: keine Prime Stats
        return []
    
    def __str__(self) -> str:
        to_string = f"Job:              {self.name}\n"
        to_string += f"Prime-Stats:      {self.prime_stats}\n"
        to_string += f"Spell-Stat:       {self.get_spell_stat()}\n"
        return to_string

if __name__ == "__main__":
    # Example usage
    #myValue = Rolls(100).roll()
    test = Job("Krieger")
    print(test)

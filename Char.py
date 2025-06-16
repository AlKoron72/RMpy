import SHORTS
from Rolls import Rolls
from Stat import Stat
import pandas as pd


def create_empty_set(self):
    for s in SHORTS.SHORTS:
        self.Stats.append(Stat(str(s.name), 0))

def create_random_set(self):
    # minimum 20
    for s in SHORTS.SHORTS:
        self.Stats.append(Stat(str(s.name), Rolls(100, minimum=20).roll()))


class Char:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.Stats = []
        create_empty_set(self)
#        for s in SHORTS.SHORTS:
#            self.Stats.append(Stat(str(s.name), Rolls(100, minimum=20).roll()))

    def __str__(self):
        to_string = f"{self.name} is {self.age} years old\n"
        for s in self.Stats:
            to_string += f"{s}\n"
        return to_string

    def create_empty_stats_df(self):
        # Erstelle einen DataFrame mit leeren Standardwerten
        data = {
            'Name': ['Nobody'] * 10,  # 10 Zeilen mit "Nobody"
            'Value': [0] * 10,  # 10 Zeilen mit 0
            'Bonus': [0] * 10  # 10 Zeilen mit 0
        }
        # Füge die Standardabkürzungen als Index hinzu
        index = []
        for s in SHORTS.SHORTS:
            index.append(str(s.name))
        return pd.DataFrame(data, index=index)


if __name__ == "__main__":
    # Example usage
    james = Char("James", 25)
    myValue = james.Stats[0].value
    print(james)

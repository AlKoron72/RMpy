import SHORTS
from Rolls import Rolls
from Stat import Stat
#from Job import Job
import pandas as pd
import importlib
from tables import dev_points, spell_points

class Char:
    def __init__(self, name: str, age: int, more_name:str = "", job: str = "Berufsloser", random_set: bool = False, race: str = "Mensch"):
        self.id = 0
        self.race = race
        self.name = name
        self.more_name = more_name
        self.age = age
        self.Stats = []  # Stats ist eine Liste von Stat-Instanzen
        if random_set:
            self.create_random_set()
        else:
            self.create_empty_set()
        # sets job from library jobs
        if job != "Berufsloser":
            # Dynamisches Importieren des Job-Moduls und der Klasse
            module = importlib.import_module(f"jobs.{job}")
            job_class = getattr(module, job)
            self.job = job_class(job)
        else:
            self.job = job  # String "Berufsloser"#
        self.hit_points_base:int = 1
        self.hit_points_total:int = self.hit_points_base
        self.hit_points_temp:int = self.hit_points_base
        self.spell_points:int = 0
        self.spell_points_temp:int = self.spell_points
#            self.Stats.append(Stat(str(s.name), Rolls(100, minimum=20).roll()))

    def __str__(self):
        to_string = f"{self.name} ist {self.age} Jahre alt.\n"
        to_string += f"Er ist ein {self.job.name}.\n"
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
    

    def create_empty_set(self):
        for s in SHORTS.SHORTS:
            self.Stats.append(Stat(str(s.name), 0))

    def create_random_set(self):
        # minimum 20
        for s in SHORTS.SHORTS:
            self.Stats.append(Stat(str(s.name), Rolls(100, minimum=20).roll()))
    
    def roll_all_max(self):
        # function to invoke max-values for all Stats
        for m in self.Stats:
            m.set_max_value(m)

    def set_race(self, race: str):
        self.race = race
        
    def set_stat_value(self, stat_short:str, value:int, set_max: bool = False):
        for s in self.Stats:
            if s.name == stat_short:
                if set_max:
                    s.max_value = value
                else:
                    print(f"({stat_short}/{value}) for: {s.name}")
                    s.value = value
                    print(f"(got: {s.value}")
    
    def get_value_for_stat(self, short: str, max: bool = False) -> int:
        return_value = 0
        for stat in self.Stats:
            if stat.name == short:
                if max:
                    return_value = stat.max_value
                else:
                    return_value = stat.value
        return return_value
    
if __name__ == "__main__":
    # Example usage
    james = Char("James", 25)
    myValue = james.Stats[0].value
    print(james)

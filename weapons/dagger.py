from weapons.master.weapon import Weapon

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger", damage=15, weight=1.0, range=1)
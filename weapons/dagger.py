from master.weapon import Weapon

class Dagger(Weapon):
    """AI is creating summary for Dagger

    Args:
        Weapon ([type]): [description]
    """
    def __init__(self):
        super().__init__(name="Dagger", damage=15, weight=1.0, range=1)
        
if __name__ == "__main__":
    dagger = Dagger()
    print(dagger.attack())
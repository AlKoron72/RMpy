from master.weapon import Weapon

class Short_bow(Weapon):
    def __init__(self):
        super().__init__(name="Sort Bow", damage=15, weight=1.0, range=25)

if __name__ == "__main__":
    short_bow = Short_bow()
    print(short_bow)
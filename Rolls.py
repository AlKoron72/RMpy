import random

"""A class to simulate dice rolls with various modifiers.

Attributes:
    sides (int): Number of sides on the die
    minimum (int): Minimum allowed roll value
    open_roll (bool): Whether rolls above 95 get an additional roll added
    fumble (int): Rolls below this value become False
"""

class Rolls:
    def __init__(self, sides:int, minimum = 0, open_roll:bool = False, fumble:int = 0):
        self.sides = sides
        self.minimum = minimum
        self.open_roll = open_roll
        self.fumble = fumble

    def __str__(self) -> str:
        return (f"Dice(d{self.sides}, "
                f"min:{self.minimum}, "
                f"open:{self.open_roll}, "
                f"fumble:<{self.fumble})")

    def roll(self):
        result = random.randint(1, self.sides)  # Now properly 1 to sides inclusive

        # if minimum
        if result < self.minimum:
            result = self.roll()

        # if open
        if self.open_roll and result > 95:
            result += self.roll()

        # fumble rate
        if result < self.fumble:
            result = False

        return result

''' testing
test = Rolls(100, open_roll=True, fumble=5)
test_list = []
for i in range(100):
    my_roll = test.roll()
    test_list.append(my_roll)

print(f"this roll: {test_list}")
print(f"min: {min(test_list)}")
print(f"max: {max(test_list)}")
print(f"avg: {sum(test_list)/len(test_list)}")
print(f"fumbles: {test_list.count(False)}")
#'''
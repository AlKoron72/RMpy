class Weapon:
    def __init__(self, name, damage, weight):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.fumble = 1  # Default fumble value
        self.range = 1
        
    def __str__(self):
        return f"Weapon: {self.name}, Damage: {self.damage}, Weight: {self.weight}, Fumble: {self.fumble}, Range: {self.range}"

    def attack(self):
        return f"{self.name} attacks with {self.damage} damage!"
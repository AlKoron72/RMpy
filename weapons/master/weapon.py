class Weapon:
    """AI is creating summary for 
    """
    def __init__(self, name: str, weight: float=1.0, range: float=1.0, damage: float=10.0):
        self.name = name
        self.damage = 10.0
        self.weight = 1.0
        self.fumble:int = 1  # Default fumble value
        self.range = 1.0
        self.damage_table = []  # Placeholder for damage table
        self.special_properties = []
        
        
    def __str__(self):
        return_value = f"Weapon: {self.name}\n"
        return_value += f"Damage: {self.damage}\n"
        return_value += f"Weight: {self.weight}\n"
        return_value += f"Fumble: {self.fumble}\n"
        return_value += f"Range: {self.range}\n"
        
        return return_value

    def attack(self):
        return f"{self.name} attacks with {self.damage} damage!"
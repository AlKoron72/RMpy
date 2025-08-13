from SHORTS import SHORTS

class Race:
    def __init__(self):
        self.name = "not a name"
        self.boni = {}
        for s in SHORTS:
            self.boni[s.name] = 0
        
    def __str__(self) -> str:
        return_value = "Boni für:\n"
        for key, value in self.boni.items():
            return_value += f"{key}: {value}\n"
        return return_value
    
if __name__ == "__main__":
    # Example usage
    racing = Race()
    print(racing)

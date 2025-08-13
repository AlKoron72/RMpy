class Skill:
    def __init__(self, name: str):
        self.name:str = name
        self.type:str = ""
        self.cost:list[int] = [2,6]
        self.points:int = 0
        self.bonus_stats:list[str] = []
        self.bonus_total:int = self.get_bonus_from_points(self.points)

    def __str__(self) -> str:
        to_string =  f"Skill:            {self.name}\n"
        to_string += f"Type:             {self.type}\n"
        to_string += f"Cost:             {self.cost}\n"
        to_string += f"Points:           {self.points}\n"
        to_string += f"Bonus-Stats:      {self.bonus_stats}\n"
        to_string += f"Bonus-Total:      {self.bonus_total}\n"
        return to_string

    @staticmethod
    def get_bonus_from_points(points: int) -> int:
        return_value = 0
        if points == 0:
            return_value = -25
        if 0 < points <= 10:
            return_value = points * 5
        return return_value

    @staticmethod
    def get_total_from_char(stat:str) -> int:
        if stat == "CO":
            return 10
        else:
            return 0

    def get_bonus_from_stats(self) -> int:
        bonus = 0
        for stat in self.bonus_stats:
            bonus += self.get_total_from_char(stat)
        bonus /= len(self.bonus_stats)
        return bonus

if __name__ == "__main__":
    # Example usage
    my_skill = Skill("test")
    print(my_skill)

    body_dev = Skill("Body-Development")
    body_dev.type = "Body"
    body_dev.cost = [1,3]
    body_dev.points = 0
    body_dev.bonus_stats = ["CO"]
    print(body_dev)
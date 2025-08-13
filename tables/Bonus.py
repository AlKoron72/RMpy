def standard_bonus(wert: int) -> int:
    # für Werte zwischen 1 und 100
    # aus der Tabelle RMC I - Seite 49
    match wert:
        case 0:
            bonus = -100
            return bonus
        case int(x) if 0 < x < 6:
            bonus = -25 + (wert - 1) * 2
            return bonus
        case int(x) if 5 < x < 11:
            bonus = -15 + (wert - 6) * 1
            return bonus
        case int(x) if 10 < x < 13:
            bonus = -10
            return bonus
        case int(x) if 12 < x < 38:
            bonus = -9 + int((wert - 13) / 3) * 1
            return bonus
        case int(x) if 37 < x < 41:
            bonus = -1
            return bonus
        case int(x) if 59 < x < 72:
            bonus = int((wert - 56) / 4) * 1
            return bonus
        case int(x) if 71 < x < 90:
            bonus = int((wert - 72) / 3) + 4
            return bonus
        case int(x) if 89 < x < 96:
            bonus = wert - 90 + 10
            return bonus
        case int(x) if 95 < x < 101:
            bonus = (wert - 96) * 2 + 17
            return bonus
        case _:
            bonus = 0
            return bonus

def bonus_100_plus(wert: int) -> int:
    # für Werte 100+
    # aus der Tabelle RMC I - Seite 52
    match wert:
        case 0:
            bonus = 25
            return bonus
        case int(x) if 0 < x < 5:
            bonus = 25 + wert * 5
            return bonus
        case int(x) if 4 < x < 10:
            bonus = 25 + 20 + (wert - 4) * 4
            return bonus
        case int(x) if 9 < x < 15:
            bonus = 25 + 20 + 20 + (wert - 9) * 3
            return bonus
        case int(x) if 14 < x < 20:
            bonus = 25 + 20 + 20 + 15 + (wert - 14) * 2
            return bonus
        case _:
            bonus = 25 + 20 + 20 + 15 + 10 + (wert - 19) * 1
            return bonus


if __name__ == "__main__":
    for x in range(1, 101):
        print(f"{x} / {standard_bonus(x)}")

    for x in range(101, 150):
        excessValue: int = x - 100
        print(f"{x} / {bonus_100_plus(excessValue)}")
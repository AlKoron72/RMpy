def return_max(value: int, roll: int) -> int:
    # Breich doppelte 100
    if value == 100 and roll == 100:
        return 101

    # Bereich [98, 99]
    if 98 <= value <= 99:
        if roll >= 98:
            return 100
        if roll >= 94:
            return 99

    # Bereich [95-97]
    if 95 <= value <= 97:
        if roll >= 99:
            return 100
        if roll >= 96:
            return 99
        if roll >= 93:
            return 98
        if roll >= 90:
            return 97

    # Bereich [90-94]
    if 90 <= value <= 94:
        if roll >= 99:
            return 100
        if roll >= 97:
            return 99
        if roll >= 95:
            return 98
        if roll >= 93:
            return 97
        if roll >= 91:
            return 96
        if roll >= 88:
            return 95
        if roll >= 84:
            return 94

    # Bereich [85-89]
    if 85 <= value <= 89:
        if roll >= 66:
            return min(89 + (roll - 66) // 4, 100)
        
    # Bereich [75-84]
    if 75 <= value <= 84:
        if roll >= 56:
            return min(75 + ((roll - 56) // 2), 99)

    # Bereich [60-74]
    if 60 <= value <= 74:
        if roll >= 56:
            return min(60 + ((roll - 31) // 5), 99)

    # Bereich [40-59]
    if 40 <= value <= 59:
        if roll >= 31:
            return min(40 + ((roll - 31) // 5) * 2, 99)

    # Bereich [25-39]
    if 25 <= value <= 39:
        if roll >= 21:
            return min(25 + ((roll - 21) // 5) * 3, 98)

    # Bereich [25-]
    if value < 25:
        return min(25 + ((roll - 1) // 5) * 5, 98)


    # Standard: Kein Wert ändert sich
    return value


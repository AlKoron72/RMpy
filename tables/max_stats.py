def return_max_simple(value: int, roll: int) -> int:
    # Breich doppelte 100
    if value == 100 and roll == 100:
        return 101
    
    if roll > value:
        return roll
    else:
        return value

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

def return_max_table(value: int, roll: int) -> int:
    # Sonderfall: 100/100
    if value == 100 and roll == 100:
        return 101

    # Finde Zeile (roll)
    row_idx = None
    for idx, (start, end) in enumerate(roll_ranges):
        if start <= roll <= end:
            row_idx = idx
            break
    if row_idx is None:
        return value  # Roll nicht gefunden

    # Finde Spalte (value)
    col_idx = None
    for idx, (v_start, v_end) in enumerate(value_ranges):
        if v_start <= value <= v_end:
            col_idx = idx
            break
    if col_idx is None:
        return value  # Value nicht gefunden

    result = table[row_idx][col_idx]
    if result is None:
        return value  # Kein Wert hinterlegt
    return result

table = [
    [25,   None, None, None, None, None, None, None, None, None],   # 01–10
    [30,   None, None, None, None, None, None, None, None, None],   # 11–20
    [35,   39,   None, None, None, None, None, None, None, None],   # 21–30
    [38,   42,   59,   None, None, None, None, None, None, None],   # 31–35
    [40,   45,   62,   None, None, None, None, None, None, None],   # 36–40
    [42,   47,   64,   None, None, None, None, None, None, None],   # 41–45
    [44,   49,   66,   None, None, None, None, None, None, None],   # 46–49
    [46,   51,   68,   None, None, None, None, None, None, None],   # 50–51
    [48,   53,   70,   None, None, None, None, None, None, None],   # 52–53
    [50,   55,   71,   None, None, None, None, None, None, None],   # 54–55
    [52,   57,   72,   74,   84,   None, None, None, None, None],   # 56–57
    [54,   59,   73,   75,   85,   None, None, None, None, None],   # 58–59
    [56,   61,   74,   76,   86,   None, None, None, None, None],   # 60–61
    [58,   63,   75,   77,   87,   None, None, None, None, None],   # 62–63
    [60,   65,   76,   78,   88,   None, None, None, None, None],   # 64–65
    [62,   67,   77,   79,   88,   89,   None, None, None, None],   # 66–67
    [64,   69,   78,   80,   89,   89,   None, None, None, None],   # 68–69
    [66,   71,   79,   81,   89,   90,   None, None, None, None],   # 70–71
    [68,   73,   80,   82,   90,   90,   None, None, None, None],   # 72–73
    [70,   75,   81,   83,   90,   91,   None, None, None, None],   # 74–75
    [72,   77,   82,   84,   91,   91,   None, None, None, None],   # 76–77
    [74,   79,   83,   85,   91,   92,   None, None, None, None],   # 78–79
    [76,   81,   84,   86,   92,   92,   None, None, None, None],   # 80–81
    [78,   83,   85,   87,   92,   93,   None, None, None, None],   # 82–83
    [80,   85,   87,   89,   93,   93,   94,   None, None, None],   # 84–85
    [82,   86,   88,   90,   93,   94,   94,   None, None, None],   # 86–87
    [84,   87,   89,   91,   94,   94,   95,   None, None, None],   # 88–89
    [86,   88,   89,   91,   94,   95,   95,   97,   None, None],   # 90
    [88,   89,   90,   92,   95,   95,   96,   97,   None, None],   # 91
    [90,   90,   91,   93,   95,   96,   96,   97,   None, None],   # 92
    [91,   91,   92,   94,   96,   96,   97,   98,   None, None],   # 93
    [92,   92,   93,   95,   96,   97,   97,   98,   99,   None],   # 94
    [93,   93,   94,   96,   97,   97,   98,   98,   99,   None],   # 95
    [94,   94,   95,   97,   97,   98,   98,   99,   99,   None],   # 96
    [95,   95,   96,   97,   98,   98,   99,   99,   99,   None],   # 97
    [96,   96,   97,   98,   98,   99,   99,   99,   100,  None],  # 98
    [97,   97,   98,   98,   99,   99,   100,  100,  100,  None],  # 99
    [98,   98,   99,   99,   99,   100,  100,  100,  100,  101],   # 100
]
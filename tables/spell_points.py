spell_pt = [-1]  # Index 0 ungenutzt

# 1–59: 0.0
spell_pt.extend([0.0] * 59)  # 1–59

# 60–61: 0.1
spell_pt.extend([0.1] * 2)   # 60–61

# 62–63: 0.2
spell_pt.extend([0.2] * 2)   # 62–63

# 64–65: 0.3
spell_pt.extend([0.3] * 2)   # 64–65

# 66–67: 0.4
spell_pt.extend([0.4] * 2)   # 66–67

# 68–69: 0.5
spell_pt.extend([0.5] * 2)   # 68–69

# 70–71: 0.6
spell_pt.extend([0.6] * 2)   # 70–71

# 72–73: 0.7
spell_pt.extend([0.7] * 2)   # 72–73

# 74–75: 0.8
spell_pt.extend([0.8] * 2)   # 74–75

# 76–77: 0.9
spell_pt.extend([0.9] * 2)   # 76–77

# 78–79: 1.0
spell_pt.extend([1.0] * 2)   # 78–79

# 80–81: 1.1
spell_pt.extend([1.1] * 2)   # 80–81

# 82–83: 1.2
spell_pt.extend([1.2] * 2)   # 82–83

# 84–85: 1.3
spell_pt.extend([1.3] * 2)   # 84–85

# 86–87: 1.4
spell_pt.extend([1.4] * 2)   # 86–87

# 88–89: 1.5
spell_pt.extend([1.5] * 2)   # 88–89

# 90–91: 1.6
spell_pt.extend([1.6] * 2)   # 90–91

# 92–93: 1.7
spell_pt.extend([1.7] * 2)   # 92–93

# 94–95: 1.8
spell_pt.extend([1.8] * 2)   # 94–95

# 96–97: 1.9
spell_pt.extend([1.9] * 2)   # 96–97

# 98–99: 2.0
spell_pt.extend([2.0] * 2)   # 98–99

# 100: 2.0
spell_pt.append(2.0)         # 100

def get_spell_pt(stat: int) -> float:
    if not 1 <= stat <= 100:
        raise ValueError("Wert muss zwischen 1 und 100 liegen.")
    return spell_pt[stat]

if __name__ == "__main__":
    print(get_spell_pt(59))   # 0.0
    print(get_spell_pt(62))   # 0.2
    print(get_spell_pt(100))  # 2.0
    
    #print(get_spell_pt(101))  # errr
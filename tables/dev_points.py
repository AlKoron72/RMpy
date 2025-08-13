def get_dev_points(wert: int) -> float:
    # für Werte zwischen 1 und 100
    # aus der Tabelle RMC I - Seite 49
    dev_points = [-1.0, 1.0, 1.3, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.7, 2.8] #0-1

    dev_points.extend([2.9] * 2)  #11-12
    dev_points.extend([3.0] * 3)  #13-15
    dev_points.extend([3.3] * 3)  #16-18
    dev_points.extend([3.6] * 3)  #19-21
    dev_points.extend([3.8] * 3)  #22-24

    dev_points.extend([4.0] * 3)  #25-27
    dev_points.extend([4.3] * 3)  #28-30
    dev_points.extend([4.6] * 2)  #31-32
    dev_points.extend([4.8] * 4)  #33-36
    dev_points.extend([5.0] * 4)  #37-40

    dev_points.extend([5.5] * 19)  #41-59

    dev_points.extend([6.0] * 4)   #60-63
    dev_points.extend([6.3] * 4)   #64-67
    dev_points.extend([6.6] * 4)   #68-71
    dev_points.extend([6.8] * 3)   #72-74
    dev_points.extend([7.0] * 3)   #75-77

    dev_points.extend([7.4] * 3)   #78-80
    dev_points.extend([7.7] * 3)   #81-83
    dev_points.extend([8.0] * 3)   #84-86
    dev_points.extend([8.2] * 3)   #87-89
    dev_points.append(8.4)         #90

    dev_points.append(8.6)         #91
    dev_points.append(8.7)         #92
    dev_points.append(8.8)         #93
    dev_points.append(8.9)         #94
    dev_points.append(9.0)         #95

    dev_points.append(9.2)         #96
    dev_points.append(9.4)         #97
    dev_points.append(9.6)         #98
    dev_points.append(9.8)         #99
    dev_points.append(10.0)        #100

    if wert > 100:
        return get_dev_points_100_plus(wert)
    else:
        return dev_points[wert]

def get_dev_points_100_plus(wert: int) -> float:
    # Werte 100+
    # aus der Tabelle RMC I - Seite 52
    return 10 + ((wert - 100) * 0.5)


if __name__ == "__main__":
    print(get_dev_points(1))
    print(get_dev_points(50))
    print(get_dev_points(100))
    print(get_dev_points(102))
    '''
    for x in range(1, 101):
        print(f"{x} / {standard_bonus(x)}")

    for x in range(101, 150):
        excessValue: int = x - 100
        print(f"{x} / {bonus_100_plus(excessValue)}")
    '''

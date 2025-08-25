import random

"""
innerhalb dieses Systems würde ich gerne ein Kampfsystem erstellen,

das Offensiv-Bonus (Skill-Wert) + Würfelwurf eines Charakters 
mit einer Waffe gegen den Defensivbonus von 1 bis 3 Gegnern bemisst

Ein Char kann dabei seine Werte erst gegen 2 Gegner gleichzeitig verteilen, 
wenn er bereits über 11 oder mehr Skill-Punkte auf diese Waffe verteilt hat, 
3 und mehr Gegner, wenn er mindestens 21 Skill-Punkte verteilt hat

Außerdem soll die Parade der Waffe den Schaden zufügen, 
der durch die Parade an Schadenspunkten verhindet wude.

Hier kann gern mit verschiedenen Klassen jongliert werden, 
um das System erweiterbar und mit verschieden Elementen kombinierbar zu machen
"""

class Weapon:
    def __init__(self, name, damage, parry, skill_points):
        self.name = name
        self.damage = damage
        self.parry = parry
        self.skill_points = skill_points

class AttackResult:
    def __init__(self, attacker, defender, hit, damage, parried):
        self.attacker = attacker
        self.defender = defender
        self.hit = hit
        self.damage = damage
        self.parried = parried

class Combatant:
    def __init__(self, char, weapon, offense_bonus, defense_bonus):
        self.char = char
        self.weapon = weapon
        self.offense_bonus = offense_bonus
        self.defense_bonus = defense_bonus
        self.hp = char.hit_points_total

    def attack_roll(self):
        return self.offense_bonus + random.randint(1, 100)

    def parry_roll(self):
        return self.weapon.parry + random.randint(1, 50)

class CombatSystem:
    def resolve_attack(self, attacker, defenders):
        results = []
        max_targets = 1
        if attacker.weapon.skill_points >= 21:
            max_targets = 3
        elif attacker.weapon.skill_points >= 11:
            max_targets = 2

        targets = defenders[:max_targets]
        split_bonus = attacker.offense_bonus // len(targets)
        for defender in targets:
            attack_value = split_bonus + random.randint(1, 100)
            defense_value = defender.defense_bonus + random.randint(1, 100)
            hit = attack_value > defense_value
            damage = attacker.weapon.damage if hit else 0
            parried = 0
            if hit and defender.weapon:
                parry_value = defender.parry_roll()
                if parry_value > damage:
                    parried = damage
                    damage = 0
                else:
                    parried = parry_value
                    damage -= parry_value
            defender.hp -= damage
            results.append(AttackResult(attacker.char, defender.char, hit, damage, parried))
        return results

# Beispiel für die Nutzung:
if __name__ == "__main__":
    from Char import Char

    attacker_char = Char("Angreifer", 30)
    defender1_char = Char("Verteidiger1", 25)
    defender2_char = Char("Verteidiger2", 28)

    attacker_weapon = Weapon("Schwert", damage=20, parry=10, skill_points=15)
    defender_weapon = Weapon("Schild", damage=0, parry=15, skill_points=5)

    attacker = Combatant(attacker_char, attacker_weapon, offense_bonus=30, defense_bonus=10)
    defender1 = Combatant(defender1_char, defender_weapon, offense_bonus=10, defense_bonus=25)
    defender2 = Combatant(defender2_char, defender_weapon, offense_bonus=10, defense_bonus=20)

    combat = CombatSystem()
    results = combat.resolve_attack(attacker, [defender1, defender2])

    for res in results:
        print(f"{res.attacker.name} greift {res.defender.name} an: {'Treffer!' if res.hit else 'Verfehlt!'} Schaden: {res.damage}, Parade: {res.parried}")
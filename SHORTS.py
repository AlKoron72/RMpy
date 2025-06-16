from enum import Enum

class SHORTS(Enum):
    AG = "Agility"
    CO = "Constitution"
    ME = "Memory"
    RE = "Reasoning"
    SD = "Self Discipline"
    EM = "Empathy"
    IN = "Intuition"
    PR = "Presence"
    QU = "Quickness"
    ST = "Strength"


if __name__ == "__main__":
    # Example usage
    for s in SHORTS:
        print(f"{s}: {s.value}")

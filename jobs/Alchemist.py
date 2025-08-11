from jobs.master.Job import Job

class Alchemist(Job):
    # standardShorts = ("ST", "QU", "PR", "IN", "EM", "SD", "RE", "ME", "CO", "AG")

    def get_prime(self) -> list[str]:
        return ["RE", "EM"]
    
    def get_spell_stat(self) -> str:
        return "IN"

if __name__ == "__main__":
    # Example usage
    #myValue = Rolls(100).roll()
    test = Alchemist("Alchemist")
    print(test)

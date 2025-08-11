from jobs.master.Job import Job

class Kleriker(Job):
    # standardShorts = ("ST", "QU", "PR", "IN", "EM", "SD", "RE", "ME", "CO", "AG")
    def get_spell_stat(self) -> str:
        return "IN"
        
    def get_prime(self) -> list[str]:
        return ["IN", "ME"]

if __name__ == "__main__":
    # Example usage
    #myValue = Rolls(100).roll()
    test = Kleriker("Kleriker")
    print(test)
    print(f"locattion {__file__}\n")

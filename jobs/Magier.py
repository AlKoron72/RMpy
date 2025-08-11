from jobs.master.Job import Job

class Magier(Job):
    # standardShorts = ("ST", "QU", "PR", "IN", "EM", "SD", "RE", "ME", "CO", "AG")

    def get_spell_stat(self) -> str:
        return "EM"
    
    def get_prime(self) -> list[str]:
        return ["RE", "EM"]
    
if __name__ == "__main__":
    # Example usage
    #myValue = Rolls(100).roll()
    test = Magier("Magier")
    print(test)
    print(f"locattion {__file__}\n")

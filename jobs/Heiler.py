from jobs.master.Job import Job

class Heiler(Job):
    def get_prime(self) -> list[str]:
        return ["IN", "ME"]
    
    def get_spell_stat(self) -> str:
        return "IN"

if __name__ == "__main__":
    # Example usage
    #myValue = Rolls(100).roll()
    test = Heiler("Heiler")
    print(Heiler)

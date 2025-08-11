from jobs.master.Job import Job

class Kämpfer(Job):
    # standardShorts = ("ST", "QU", "PR", "IN", "EM", "SD", "RE", "ME", "CO", "AG")

    def get_prime(self) -> list[str]:
        return ["ST", "CO"]
    
if __name__ == "__main__":
    # Example usage
    #myValue = Rolls(100).roll()
    test = Kämpfer("Kämpfer")
    print(test)

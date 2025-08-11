from jobs.master.Job import Job

class Dieb(Job):
    def get_prime(self) -> list[str]:
        return ["QU", "AG"]

if __name__ == "__main__":
    # Example usage
    #myValue = Rolls(100).roll()
    test = Dieb("Dieb")
    print(test)

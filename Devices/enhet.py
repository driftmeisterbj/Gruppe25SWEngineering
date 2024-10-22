class Enhet:
    def __init__(self, navn):
        self.navn = navn
        self.på = False

    def skru_av(self):
        self.på = False
        print(f"{self.navn} er nå av.")

    def skru_på(self):
        self.på = True
        print(f"{self.navn} er nå på.")

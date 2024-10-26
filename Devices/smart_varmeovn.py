from Deivce import Devices

class SmartVarmeovn(Enhet):
    def __init__(self, prod_id, navn, brand, temperatur=20):
        super().__init__(prod_id, navn, brand)
        self.temperatur = temperatur
        self.på = False
        
    def skru_på(self):
        self.på = True
        print(f"{self.navn} er nå på.")

    def skru_av(self):
        self.på = False
        print(f"{self.navn} er nå av.")

    def sett_temperatur(self, ny_temp):
        try:
            ny_temp = int(ny_temp)
            if 15 <= ny_temp <= 30:
                self.temperatur = ny_temp
                print(f"{self.navn} er nå satt til {self.temperatur} grader.")
            else:
                print("Ugyldig temperatur! Temperaturen må være mellom 15 og 30 grader.")
        except ValueError:
            print("Vennligst skriv inn en gyldig heltallverdi for temperaturen.")

    def status(self):
        if self.på:
            print(f"{self.navn} ({self.brand}) er på, temperatur: {self.temperatur} grader.")
        else:
            print(f"{self.navn} ({self.brand}) er av.")

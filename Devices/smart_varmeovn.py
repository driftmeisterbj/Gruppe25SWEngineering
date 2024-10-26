from Deivce import Device

class SmartVarmeovn(Device):
    def __init__(self, prod_id, name, brand, temperatur=20):
        super().__init__(prod_id, name, brand)
        self.temperatur = temperatur
        self.on = False
        
    def skru_på(self):
        self.on = True
        print(f"{self.navn} er nå på.")

    def skru_av(self):
        self.on = False
        print(f"{self.navn} er nå av.")

    def sett_temperatur(self, ny_temp):
        try:
            ny_temp = int(ny_temp)
            if 15 <= ny_temp <= 30:
                self.temperatur = ny_temp
                print(f"{self.name} er nå satt til {self.temperatur} grader.")
            else:
                print("Ugyldig temperatur! Temperaturen må være mellom 15 og 30 grader.")
        except ValueError:
            print("Vennligst skriv inn en gyldig heltallverdi for temperaturen.")

    def status(self):
        if self.on:
            print(f"{self.name} ({self.brand}) er på, temperatur: {self.temperatur} grader.")
        else:
            print(f"{self.name} ({self.brand}) er av.")

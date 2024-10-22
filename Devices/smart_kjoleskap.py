from enhet import Enhet

class SmartKjøleskap(Enhet):
    def __init__(self, navn, temperatur=4):
        super().__init__(navn)
        self.temperatur = temperatur
        self.på = False  # Start med kjøleskapet av

    def sett_temperatur(self, ny_temp):
        try:
            ny_temp = int(ny_temp)
            if 2 <= ny_temp <= 12:
                self.temperatur = ny_temp
                print(f"{self.navn} er nå satt til {self.temperatur} grader.")
            else:
                print("Ugyldig temperatur! Temperaturen må være mellom 2 og 12 grader.")
        except ValueError:
            print("Vennligst skriv inn en gyldig heltallverdi for temperaturen.")

    def status(self):
        if self.på:
            print(f"{self.navn} er på, temperatur: {self.temperatur} grader.")
        else:
            print(f"{self.navn} er av.")

from enhet import Enhet

class SmartLys(Enhet):
    def __init__(self, navn, lysstyrke=5):
        super().__init__(navn)
        self.lysstyrke = lysstyrke
        self.på = False
        
    def skru_på(self):
        self.på = True
        print(f"{self.navn} er nå på.")

    def skru_av(self):
        self.på = False
        print(f"{self.navn} er nå av.")

    def sett_lysstyrke(self, ny_lysstyrke):
        try:
            ny_lysstyrke = int(ny_lysstyrke)  # Konvertere til heltall
            if 1 <= ny_lysstyrke <= 10:
                self.lysstyrke = ny_lysstyrke
                print(f"{self.navn} er nå satt til lysstyrke {self.lysstyrke}.")
            else:
                print("Ugyldig lysstyrke! Lysstyrken må være mellom 1 og 10.")
        except ValueError:
            print("Vennligst skriv inn en gyldig heltallverdi for lysstyrken.")

    def status(self):
        if self.på:
            print(f"{self.navn} er på, lysstyrke: {self.lysstyrke}.")
        else:
            print(f"{self.navn} er av.")

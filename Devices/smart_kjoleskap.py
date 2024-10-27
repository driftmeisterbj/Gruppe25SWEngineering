from Device import Device

class SmartKjøleskap(Device):
    def __init__(self, prod_id, name, brand, category, temperatur=4):
        super().__init__(name, prod_id, brand, category)
        self.temperatur = temperatur
        self.on = False

    def sett_temperatur(self, ny_temp):
        try:
            ny_temp = int(ny_temp)
            if 2 <= ny_temp <= 12:
                self.temperatur = ny_temp
                print(f"{self.name} er nå satt til {self.temperatur} grader.")
            else:
                print("Ugyldig temperatur! Temperaturen må være mellom 2 og 12 grader.")
                
        except ValueError:
            raise ValueError("Vennligst skriv inn en gyldig heltallverdi for temperaturen.")
            

    def status(self):
        if self.on:
            return f"{self.name} ({self.brand}) er på, temperatur: {self.temperatur} grader."
        else:
            return f"{self.name} ({self.brand}) er av."

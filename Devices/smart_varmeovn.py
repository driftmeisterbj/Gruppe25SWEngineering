from Device import Device

class SmartVarmeovn(Device):
    def __init__(self, prod_id, name, brand, category, temperatur=20):
        super().__init__(prod_id, name, brand, category)
        self.temperatur = temperatur
        self.on = False

    # Function to set new temperature
    # Recive user input and accept or deny based on if it is invalid or not
    # Noteify the user if there is any error and to try again 
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

    # Method to display current status
    # Print out if it is on and other information or that it is off.
    def status(self):
        if self.on:
            print(f"{self.name} ({self.brand}) er på, temperatur: {self.temperatur} grader.")
        else:
            print(f"{self.name} ({self.brand}) er av.")

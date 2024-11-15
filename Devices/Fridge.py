from Device import Device

class Fridge(Device):
    def __init__(self, prod_id, name, brand, temperature=4):
        super().__init__(prod_id, name, brand, "Fridge")
        self.temperature = temperature


    def set_temperature(self, new_temperature):
        if new_temperature == '+':
            if not self.temperature >= 12:
                self.temperature += 1
        elif new_temperature == '-':
            if not self.temperature <= 2:
                self.temperature -= 1


"""
    def set_temperature(self, new_temp):
        try:
            new_temp = int(new_temp)
            if 2 <= new_temp <= 12:
                self.temperature = new_temp
                print(f"{self.brand} {self.name} is now set to {self.temperature} Celcius")
            else:
                print("Invalid temperature, must be between 2 and 12 degrees")
                
        except ValueError:
            raise ValueError("Vennligst skriv inn en gyldig heltallverdi for temperaturen.")
           """

       

"""
    def status(self):
        if self.on:
            return f"{self.brand} {self.name} is on. Current temperature: {self.temperature} Celcius"
        else:
            return f"{self.brand} {self.name} is off"
"""
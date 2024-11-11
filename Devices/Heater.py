from Device import Device

class Heater(Device):
    def __init__(self,prod_id,name,brand,temperature=15):
        super().__init__(prod_id,name,brand, "Heater")
        self.temperature = temperature

    # Function to set new temperaturee
    # Recive user input and accept or deny based on if it is invalid or not
    # Noteify the user if there is any error and to try again
    def set_temperature(self, new_temp):
        try:
            new_temp = int(new_temp)
            if 15 <= new_temp <= 30:
                self.temperature = new_temp
                print(f"{self.brand} {self.name} is now set to {self.temperature} Celcius.")
            else:
                print("Invalid temperature, must be between 15 and 30 degrees.")
        except ValueError:
            raise ValueError("Please input a valid number")

    # Method to display current status
    # Print out if it is on and other information or that it is off.
    def status(self):
        if self.on:
            return f"{self.brand} {self.name} is on, temperature: {self.temperature} celsius."
        else:
            return f"{self.brand} {self.name} is off."

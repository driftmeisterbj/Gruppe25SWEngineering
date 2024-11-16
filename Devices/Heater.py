from Device import Device

class Heater(Device):
    def __init__(self,prod_id,name,brand,temperature=15):
        super().__init__(prod_id,name,brand, "Heater")
        self.temperature = temperature

    def set_temperature(self, new_temperature):
        if new_temperature == '+':
            if not self.temperature >= 30:
                self.temperature += 1
        elif new_temperature == '-':
            if not self.temperature <= 15:
                self.temperature -= 1

    def getDict(self):
        device_dict = {
            "prod_id": self.prod_id,
            "name": self.name,
            "brand": self.brand,
            "category": self.category,
            "on": self.on,
            "temperature": self.temperature
        }

        return device_dict
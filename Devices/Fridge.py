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
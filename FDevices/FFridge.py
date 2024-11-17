from FDevice import Device

class Fridge(Device):
    def __init__(self, prod_id, name, brand, on=False, temperature=4):
        super().__init__(prod_id, name, brand, "Fridge", on)
        self.temperature = temperature


    def set_temperature(self, new_temperature):
        if new_temperature == '+':
            if not self.temperature >= 12:
                self.temperature += 1
        elif new_temperature == '-':
            if not self.temperature <= 2:
                self.temperature -= 1

    def get_dict(self):
        device_dict = super().get_dict()
        device_dict['temperature'] = self.temperature

        return device_dict
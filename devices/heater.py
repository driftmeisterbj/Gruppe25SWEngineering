from device_class import Device

class Heater(Device):
    def __init__(self, prod_id, name, brand, on=False, temperature=15):
        super().__init__(prod_id,name,brand, "Heater", on)
        self.temperature = temperature

    def set_temperature(self, new_temperature):
        if new_temperature == '+':
            if not self.temperature >= 30:
                self.temperature += 1
        elif new_temperature == '-':
            if not self.temperature <= 15:
                self.temperature -= 1

    def get_dict(self):
        device_dict = super().get_dict()
        device_dict['temperature'] = self.temperature

        return device_dict
from Device import Device
class Light(Device):
    def __init__(self, prod_id, name, brand, on=False, brightness=5):
        super().__init__(prod_id,name,brand, "Light", on)
        self.brightness = brightness
        #self.on = False
        


    def set_brightness(self, new_brightness):
        if new_brightness == '+':
            if not self.brightness >= 10:
                self.brightness += 1
        elif new_brightness == '-':
            if not self.brightness <= 0:
                self.brightness -= 1

    def get_dict(self):
        device_dict = super().get_dict()
        device_dict['brightness'] = self.brightness

        return device_dict
    
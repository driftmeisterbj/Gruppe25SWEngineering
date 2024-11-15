from Device import Device
class Light(Device):
    def __init__(self,prod_id,name,brand,brightness=5):
        super().__init__(prod_id,name,brand, "Light")
        self.brightness = brightness
        #self.on = False
        


    def set_brightness(self, new_brightness):
        if new_brightness == '+':
            if not self.brightness >= 10:
                self.brightness += 1
        elif new_brightness == '-':
            if not self.brightness <= 0:
                self.brightness -= 1

    def getDict(self):
        device_dict = {
            "prod_id": self.prod_id,
            "name": self.name,
            "brand": self.brand,
            "category": self.category,
            "on": self.on,
            "brightness": self.brightness
        }

        return device_dict
    

"""
    def status(self):
        if self.on:
            return f"{self.brand} {self.name} is turned on, brightness: {self.brightness}"
        else:
            return f"{self.brand} {self.name} is off."
"""
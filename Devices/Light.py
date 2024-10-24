from Device import Device
class Light(Device):
    def __init__(self,prod_id,name,brand, on, brightness=5):
        super().__init__(prod_id,name,brand, on, "Light")
        self.brightness = brightness
        #self.on = False
        
    def set_brightness(self, new_brightness):
        try:
            new_brightness = int(new_brightness)  # Konvertere til heltall
            if 1 <= new_brightness <= 10:
                self.brightness = new_brightness
                print(f"{self.brand} {self.name} brightness set to: {self.brightness}")
            elif new_brightness < 0:
                self.brightness = 0
                print(f"{self.brand} {self.name} brightness set to: {self.brightness}")
            elif new_brightness > 10:
                self.brightness = 10
                print(f"{self.brand} {self.name} brightness set to: {self.brightness}")


        except ValueError:
            print("Brightness must be number")

    def status(self):
        if self.on:
            print(f"{self.brand} {self.name} is turned on, brightness: {self.brightness}")
        else:
            print(f"{self.brand} {self.name} is off.")

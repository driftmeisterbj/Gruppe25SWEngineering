class Device:
    def __init__(self, prod_id, name, brand, category):
        self.prod_id = prod_id
        self.name = name
        self.brand = brand
        self.category = category
        self.on = False

    def turn_off_device(self):
        self.on = False

    def turn_on_device(self):
        self.on = True

    def getDict(self):
        device_dict = {
            "prod_id": self.prod_id,
            "name": self.name,
            "brand": self.brand,
            "category": self.category,
        }

        return device_dict

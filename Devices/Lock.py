from Device import Device

class Lock(Device):
    def __init__(self, prod_id, name, brand, status="Unlocked", entry_code="0727"):
        super().__init__(prod_id, name, brand, "Lock")
        self.status = status
        self.entry_code = entry_code

    def set_entry_code(self, new_code):
        if isinstance(new_code, str) and new_code.isdigit() and len(new_code) == 4:
            self.entry_code = new_code
            return True
        else:
            return False

    def lock(self):
        self.status = "Locked"
        print(f"{self.brand} {self.name} is now locked")
    def unlock(self,entered_code):
        if entered_code == self.entry_code:
            self.status = "Unlocked"
            return True
        else:
            return False
        
    def getDict(self):
        device_dict = {
            "prod_id": self.prod_id,
            "name": self.name,
            "brand": self.brand,
            "category": self.category,
            "on": self.on,
            "status": self.status,
            "entry_code": self.entry_code
        }

        return device_dict

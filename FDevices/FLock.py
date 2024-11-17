from Device import Device

class Lock(Device):
    def __init__(self, prod_id, name, brand, on=False, status="Unlocked", entry_code="0727"):
        super().__init__(prod_id, name, brand, "Lock", on)
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
    def unlock(self,entered_code):
        if entered_code == self.entry_code:
            self.status = "Unlocked"
            return True
        else:
            return False
        
    def get_dict(self):
        device_dict = super().get_dict()
        device_dict['status'] = self.status
        device_dict['entry_code'] = self.entry_code

        return device_dict

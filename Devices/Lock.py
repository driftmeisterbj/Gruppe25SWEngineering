from Device import Device

class SmartLock(Device):
    def __init__(self, prod_id, name, brand, status="Unlocked", entry_code="0727"):
        super().__init__(prod_id, name, brand, "Smart Lock")
        self.status = status
        self.entry_code = entry_code

    def set_entry_code(self, new_code):
        if isinstance(new_code, str) and new_code.isdigit() and len(new_code) == 4:
            self.entry_code = new_code
            print(f"Entry code has been updated to: {self.entry_code}")
        else:
            print("Invalid entry code Must be a 4-digit number")

    def lock(self):
        self.status = "Locked"
        print(f"{self.brand} {self.name} is now locked")
    
    def unlock(self, entered_code):
        if entered_code == self.entry_code:
            self.status = "Unlocked"  # Ensure consistent casing
            print(f"{self.brand} {self.name} is now unlocked")
        else:
            print("Incorrect entry code. The lock remains locked")

    def get_status(self):
        return f"{self.brand}, {self.name} is currently {self.status}."

from Device import Device

class Camera(Device):
    def __init__(self, prod_id, name, brand, resolution="1080p", status="Inactive", motion_detection=False):
        super().__init__(prod_id, name, brand, "Camera")
        self.resolution = resolution
        self.status = status
        self.motion_detection = motion_detection

    def set_resolution(self, new_resolution):
        valid_resolutions = ["720p", "1080p", "4K"]
        if new_resolution in valid_resolutions:
            self.resolution = new_resolution
            print(f"Resolution has been updated to: {self.resolution}")
        else:
            print("Invalid resolution. Choose from: 720p, 1080p, or 4K.")

    def activate(self):
        self.status = "Active"
        print(f"{self.brand} {self.name} is now active.")
    
    def deactivate(self):
        self.status = "Inactive"
        print(f"{self.brand} {self.name} is now inactive.")
    
    def toggle_motion_detection(self):
        self.motion_detection = not self.motion_detection
        state = "enabled" if self.motion_detection else "disabled"
        print(f"Motion detection has been {state}.")

    def status(self):
        motion_state = "enabled" if self.motion_detection else "disabled"
        return f"{self.brand} {self.name} is currently {self.status}. Resolution: {self.resolution}. Motion Detection: {motion_state}."

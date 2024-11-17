from Device import Device

class Camera(Device):
    def __init__(self, prod_id, name, brand, on=False, resolution="1080p", status="Inactive", motion_detection=False):
        super().__init__(prod_id, name, brand, "Camera", on)
        self.resolution = resolution
        self.status = status    
        self.motion_detection = motion_detection

    def set_resolution(self, new_resolution):
        valid_resolutions = ["180p","240p","480p","720p", "1080p","1440p","4K"]

        current_index = valid_resolutions.index(self.resolution)

        if new_resolution == '+' and current_index < len(valid_resolutions)-1:
            self.resolution = valid_resolutions[current_index+1]
        #index sjekken stopper den fra å gå rundt i sirkler når den når -1 
        elif new_resolution == '-' and current_index > 0:
            self.resolution = valid_resolutions[current_index-1]


    def activate(self):
        self.status = "Active"
    
    def deactivate(self):
        self.status = "Inactive"
    
    def toggle_motion_detection(self):
        if not self.motion_detection:
            self.motion_detection = True
        else:
            self.motion_detection = False

    def get_dict(self):
        device_dict = super().get_dict()
        device_dict['resolution'] = self.resolution
        device_dict['status'] = self.status
        device_dict['motion_detection'] = self.motion_detection

        return device_dict

from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def reset_database(self):
        pass

    @abstractmethod
    def read_database(self):
        pass

    @abstractmethod
    def is_username_taken(self, username):
        pass

    @abstractmethod
    def is_username_valid(self, username):
        pass

    @abstractmethod
    def is_password_valid(self, password):
        pass

    @abstractmethod
    def is_email_taken(self, email):
        pass

    @abstractmethod
    def is_email_valid(self, email):
        pass

    @abstractmethod
    def add_user(self, username, password, email):
        pass

    @abstractmethod
    def is_device_valid(self, device):
        pass

    @abstractmethod
    def find_user_index(self, username):
        pass

    @abstractmethod
    def add_device_to_user(self, username, device):
        pass

    @abstractmethod
    def find_device_list_user(self, username):
        pass

    @abstractmethod
    def remove_duplicate_devices_from_user(self, username):
        pass

    @abstractmethod
    def create_new_device(self, prod_id, name, brand, category):
        pass

    @abstractmethod
    def delete_device_from_user(self, username, device):
        pass

    @abstractmethod
    def recreate_device_object(self, device_dict):
        pass

    @abstractmethod
    def update_device_data(self, username, device):
        pass

    @abstractmethod
    def get_current_user(self, username):
        pass

    @abstractmethod
    def add_device_to_current_user(self, current_user, new_device):
        pass

    @abstractmethod
    def get_device_object(self, username, device_name, device_brand):
        pass

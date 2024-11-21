from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def is_username_taken(self, username):
        pass

    @abstractmethod
    def is_email_taken(self, email):
        pass

    @abstractmethod
    def add_user(self, username, password, email):
        pass

    @abstractmethod
    def get_user(self, username):
        pass

    @abstractmethod
    def add_device_to_user(self, username, device):
        pass

    @abstractmethod
    def find_device_list_user(self, username):
        pass

    @abstractmethod
    def update_device_data(self, username, device):
        pass

    @abstractmethod
    def delete_device_from_user(self, username, device):
        pass

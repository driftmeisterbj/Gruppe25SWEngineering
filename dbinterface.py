from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def reset_database(self):
        """
        Reset the database to its initial state.
        Typically used for testing purposes.
        """
        pass

    @abstractmethod
    def read_database(self):
        """
        Read the entire database and return its content.
        """
        pass

    @abstractmethod
    def is_username_taken(self, username):
        """
        Check if the given username already exists in the database.

        :param username: The username to check.
        :return: True if the username is taken, False otherwise.
        """
        pass

    @abstractmethod
    def is_username_valid(self, username):
        """
        Validate the username based on predefined rules.

        :param username: The username to validate.
        :return: True if valid, or an error message string if invalid.
        """
        pass

    @abstractmethod
    def is_password_valid(self, password):
        """
        Validate the password based on predefined rules.

        :param password: The password to validate.
        :return: True if valid, or an error message string if invalid.
        """
        pass

    @abstractmethod
    def is_email_taken(self, email):
        """
        Check if the given email is already registered in the database.

        :param email: The email to check.
        :return: True if the email is taken, False otherwise.
        """
        pass

    @abstractmethod
    def is_email_valid(self, email):
        """
        Validate the email address based on predefined rules.

        :param email: The email to validate.
        :return: True if valid, or an error message string if invalid.
        """
        pass

    @abstractmethod
    def add_user(self, username, password, email):
        """
        Add a new user to the database.

        :param username: The username of the new user.
        :param password: The password for the new user.
        :param email: The email address of the new user.
        :return: True if the user was added successfully, or an error message string if not.
        """
        pass

    @abstractmethod
    def is_device_valid(self, device):
        """
        Validate the device object to ensure it contains all required fields.

        :param device: The device object to validate.
        :return: True if valid, False otherwise.
        """
        pass

    @abstractmethod
    def find_user_index(self, username):
        """
        Find the index of a user in the database list.

        :param username: The username to find.
        :return: The index of the user if found, -1 otherwise.
        """
        pass

    @abstractmethod
    def add_device_to_user(self, username, device):
        """
        Add a device to a user's device list.

        :param username: The username of the user.
        :param device: The device object to add.
        :return: True if successful, False if user not found, or an error message string.
        """
        pass

    @abstractmethod
    def find_device_list_user(self, username):
        """
        Retrieve the list of devices associated with a user.

        :param username: The username of the user.
        :return: A list of devices, or an empty list if user not found.
        """
        pass

    @abstractmethod
    def remove_duplicate_devices_from_user(self, username):
        """
        Remove duplicate devices from a user's device list.

        :param username: The username of the user.
        :return: True if successful, False if user not found.
        """
        pass

    @abstractmethod
    def create_new_device(self, prod_id, name, brand, category):
        """
        Create a new device object based on the category.

        :param prod_id: The product ID of the device.
        :param name: The name of the device.
        :param brand: The brand of the device.
        :param category: The category of the device.
        :return: The device object if successful, False if category not implemented.
        """
        pass

    @abstractmethod
    def delete_device_from_user(self, username, device):
        """
        Delete a device from a user's device list.

        :param username: The username of the user.
        :param device: The device object to delete.
        :return: True if successful, False if user not found, or an error message string.
        """
        pass

    @abstractmethod
    def recreate_device_object(self, device_dict):
        """
        Recreate a device object from its dictionary representation.

        :param device_dict: The dictionary containing device data.
        :return: The device object if successful, False if category not recognized.
        """
        pass

    @abstractmethod
    def update_device_data(self, username, device):
        """
        Update the data of a device in the user's device list.

        :param username: The username of the user.
        :param device: The device object with updated data.
        """
        pass

    @abstractmethod
    def get_current_user(self, username):
        """
        Get the current user's data.

        :param username: The username of the user.
        :return: A dictionary containing the user's data.
        """
        pass

    @abstractmethod
    def add_device_to_current_user(self, current_user, new_device):
        """
        Add a device to the current user's device list.

        :param current_user: The current user's data dictionary.
        :param new_device: The new device object to add.
        :return: None
        """
        pass

    @abstractmethod
    def get_device_object(self, username, device_name, device_brand):
        """
        Retrieve a device object for a user based on device name and brand.

        :param username: The username of the user.
        :param device_name: The name of the device.
        :param device_brand: The brand of the device.
        :return: The device object if found, False otherwise.
        """
        pass

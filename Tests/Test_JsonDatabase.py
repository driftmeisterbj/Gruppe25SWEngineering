import unittest
from unittest import mock, TestCase
import sys
import os


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(project_root)

from jsondb import JsonDatabase

path = os.path.join(os.path.dirname(__file__), "Devices")
sys.path.append(path)
from Devices import Fridge, Heater, Lock, Light, Camera, Device
class TestJsonDatabase(unittest.TestCase):
    def setUp(self):
        self.database = JsonDatabase("test")
    
    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tester for is_username_taken()
    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
            {
                "username": "TakenName",
                "password": "p",
                "email": "1@2.3",
                "devices": []
            }
        ])
    def test_is_username_taken_true(self, mock):
        check_name = self.database.is_username_taken("TakenName")
        self.assertEqual(check_name, True)

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
            {
                "username": "TakenName",
                "password": "p",
                "email": "1@2.3",
                "devices": []
            }
        ])
    def test_is_username_taken_false(self, mock):
        check_name = self.database.is_username_taken("NonTakenName")
        self.assertEqual(check_name, False)

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
            {
                "username": "TakenName",
                "password": "p",
                "email": "1@2.3",
                "devices": []
            }
        ])
    def test_is_username_taken_lowercase(self, mock):
        check_name = self.database.is_username_taken("takenName")
        self.assertEqual(check_name, True)
    
    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tester for is_username_valid()
    def test_is_username_valid_true(self):
        username = "GyldigBruker33"
        username_check = self.database.is_username_valid(username)
        self.assertEqual(username_check, True)

    def test_is_username_valid_short(self):
        username = "b1"
        username_check = self.database.is_username_valid(username)
        self.assertEqual(username_check, 'Name: "b1" failed - Username can not be shorter than 3 characters')

    def test_is_username_valid_long(self):
        username = "VeeeeeeeeeeeeeeeeeldigLaaaaaaaaaaaaaangtNaaaaaaaaaaaaavn"
        username_check = self.database.is_username_valid(username)
        self.assertEqual(username_check, 'Name: "VeeeeeeeeeeeeeeeeeldigLaaaaaaaaaaaaaangtNaaaaaaaaaaaaavn" failed - Username can not be longer than 25 characters')

    def test_is_username_valid_illegal_character(self):
        username = "NestenGyldigBrukernavn;"
        username_check = self.database.is_username_valid(username)
        self.assertEqual(username_check, 'Username contains illegal character: " ; "')

    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tester for is_password_valid()
    def test_is_password_valid_true(self):
        password = "Gyldig_passord69"
        password_check = self.database.is_password_valid(password)
        self.assertEqual(password_check, True)

    def test_is_password_valid_short(self):
        password = "P12"
        password_check = self.database.is_password_valid(password)
        self.assertEqual(password_check, 'Password cannot be shorter than 4 characters')

    def test_is_password_valid_long(self):
        password = "TheAbsolutelyLongestPasswordInTheHistoryOfTheWorld696969696969696969696969696969699696969669699696996996969696969696969699696969"
        password_check = self.database.is_password_valid(password)
        self.assertEqual(password_check, 'Password cannot be longer than 45 characters')

    def test_is_password_valid_missing_lowercase(self):
        password = "JEGELSKERCAPSLOCK123"
        password_check = self.database.is_password_valid(password)
        self.assertEqual(password_check, 'Password must contain at least one lowercase letter')

    def test_is_password_valid_missing_uppercase(self):
        password = "jeghatercapslock123"
        password_check = self.database.is_password_valid(password)
        self.assertEqual(password_check, 'Password must contain at least one uppercase letter')

    def test_is_password_valid_missing_number(self):
        password = "JegHaterTALL!!"
        password_check = self.database.is_password_valid(password)
        self.assertEqual(password_check, 'Password must contain at least one number')

    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tester for is_email_taken()

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
            {
                "username": "TakenName",
                "password": "p",
                "email": "epost@epost.com",
                "devices": []
            }
        ])
    def test_is_email_taken_false(self, mock):
        check_email = self.database.is_email_taken("epost123@mail.com")
        self.assertEqual(check_email, False)

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
            {
                "username": "TakenName",
                "password": "p",
                "email": "epost@epost.com",
                "devices": []
            }
        ])
    def test_is_email_taken_true(self, mock):
        check_email = self.database.is_email_taken("epost@epost.com")
        self.assertEqual(check_email, True)

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
            {
                "username": "TakenName",
                "password": "p",
                "email": "epost@epost.com",
                "devices": []
            }
        ])
    def test_is_email_taken_uppercase(self, mock):
        check_email = self.database.is_email_taken("EPOST@EPOST.COM")
        self.assertEqual(check_email, True)   

    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tester for is_email_valid()
    def test_is_email_valid_true(self):
        email = "gyldig@epost.yep"
        email_check = self.database.is_email_valid(email)
        self.assertEqual(email_check, True)

    def test_is_email_valid_illegal_char(self):
        email = "nesten]gyldig@epost.yep"
        email_check = self.database.is_email_valid(email)
        self.assertEqual(email_check, 'ERROR - Illegal character " ] " in email adress')

    def test_is_email_valid_no_at(self):
        email = "nestengyldigepost.yep"
        email_check = self.database.is_email_valid(email)
        self.assertEqual(email_check, 'Email MUST contain the character " @ "')

    def test_is_email_valid_too_many_at(self):
        email = "nesten@gyldig@epost.yep"
        email_check = self.database.is_email_valid(email)
        self.assertEqual(email_check, 'Email contains too many instances of the char " @ ", you can only use this character ONCE')

    def test_is_email_valid_true_no_puntuation(self):
        email = "nestengyldig@epostyep"
        email_check = self.database.is_email_valid(email)
        self.assertEqual(email_check, 'Email MUST contain the character " . "')

    def test_is_email_valid_wrong_punctuation(self):
        email = "nesten.gyldig@epostyep"
        email_check = self.database.is_email_valid(email)
        self.assertEqual(email_check, 'ERROR - The character " . " MUST appear at least once after the character " @ " in the email adress')
    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tests for add_user_to_json()
    
    @mock.patch("jsondb.JsonDatabase.is_username_valid", return_value=True)
    @mock.patch("jsondb.JsonDatabase.is_username_taken", return_value=False)
    @mock.patch("jsondb.JsonDatabase.is_password_valid", return_value=True)
    @mock.patch("jsondb.JsonDatabase.is_email_valid", return_value=True)
    @mock.patch("jsondb.JsonDatabase.is_email_taken", return_value=False)
    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                {
                    "username": "User1",
                    "password": "password",
                    "email": "epost@epost.com",
                    "devices": []
                }, {
                    "username": "User2",
                    "password": "password",
                    "email": "epost@epost.com",
                    "devices": []
                }
            ])
    def test_add_user_to_json(self, mock1, mock2, mock3, mock4, mock5, mock6):
        user_added = self.database.add_user_to_json("Username", "Password123", "e@epost.com")
        self.assertEqual(user_added, True)
    

    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tests for is_device_valid()
    def test_is_device_valid_true(self):
        device = Device.Device(123, "Gyldig", "Enhet", "Test")
        device_check = self.database.is_device_valid(device)
        self.assertEqual(device_check, True)


    # ----------------------------------------
    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tests for find_user_index()
    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                {
                    "username": "User1",
                    "password": "password",
                    "email": "epost@epost.com",
                    "devices": []
                }, {
                    "username": "User2",
                    "password": "password",
                    "email": "epost@epost.com",
                    "devices": []
                }
            ])
    def test_find_user_index_0(self, mock):
        check_index = self.database.find_user_index("User1")
        self.assertEqual(check_index, 0) 

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                    {
                        "username": "User1",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }, {
                        "username": "User2",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }
                ])
    def test_find_user_index_1(self, mock):
        check_index = self.database.find_user_index("User2")
        self.assertEqual(check_index, 1) 

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                    {
                        "username": "User1",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }, {
                        "username": "User2",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }
                ])
    def test_find_user_index_not_found(self, mock):
        check_index = self.database.find_user_index("User3")
        self.assertEqual(check_index, -1)   
    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tests for add_device_to_user()
    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                    {
                        "username": "User1",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }, {
                        "username": "User2",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }
                ])
    def test_add_device_to_user_added(self, mock):
        device = Device.Device(123, "Gyldig", "Enhet", "Test")
        
        username = "User1"
        add_device = self.database.add_device_to_user(username, device)
        self.assertEqual(add_device, True)

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                    {
                        "username": "User1",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }, {
                        "username": "User2",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }
                ])
    @mock.patch("jsondb.JsonDatabase.is_device_valid", return_value=False)
    def test_add_device_to_user_invalid_device(self, mock, mock2):
        device = {}
        username = "User1"
        add_device = self.database.add_device_to_user(username, device)
        self.assertEqual(add_device, "Device invalid")

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                    {
                        "username": "User1",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }, {
                        "username": "User2",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }
                ])
    @mock.patch("jsondb.JsonDatabase.find_user_index", return_value=-1)
    def test_add_device_to_user_cannot_find_user(self, mock, mock2):
        device = Device.Device(123, "Gyldig", "Enhet", "Test")
        username = "User1"
        add_device = self.database.add_device_to_user(username, device)
        self.assertEqual(add_device, False)

    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tests for find_device_list_user()
    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                    {
                        "username": "User1",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": [{
                            "prod_id": 123,
                            "name": "Gyldig",
                            "brand": "Enhet",
                            "category": "Test"
                        }]
                    }, {
                        "username": "User2",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }
                ])
    @mock.patch("Device.Device.getDict", return_value={
                            "prod_id": 123,
                            "name": "Gyldig",
                            "brand": "Enhet",
                            "category": "Test"
                        })
    def test_find_device_list_user_found(self, mock, mock2):
        device_list=[{
                            "prod_id": 123,
                            "name": "Gyldig",
                            "brand": "Enhet",
                            "category": "Test"
                        }]
        username = "User1"
        find_device_list = self.database.find_device_list_user(username)
        self.assertEqual(find_device_list, device_list)

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                    {
                        "username": "User1",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": [{
                            "prod_id": 123,
                            "name": "Gyldig",
                            "brand": "Enhet",
                            "category": "Test"
                        }]
                    }, {
                        "username": "User2",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }
                ])
    def test_find_device_list_user_no_user_found(self, mock):
        username = "InvalidUser"
        find_device_list = self.database.find_device_list_user(username)
        self.assertEqual(find_device_list, [])

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                    {
                        "username": "User1",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": [{
                            "prod_id": 123,
                            "name": "Gyldig",
                            "brand": "Enhet",
                            "category": "Test"
                        }]
                    }, {
                        "username": "User2",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }
                ])
    def test_find_device_list_user_no_device_list(self, mock):
        username = "User2"
        find_device_list = self.database.find_device_list_user(username)
        self.assertEqual(find_device_list, [])
        
    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tests for remove_duplicate_devices_from_user()
    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                    {
                        "username": "User1",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": [{
                            "prod_id": 123,
                            "name": "Gyldig",
                            "brand": "Enhet",
                            "category": "Test"
                        }]
                    }, {
                        "username": "User2",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }
                ])
    def test_remove_duplicate_devices_from_user_removed(self, mock):
        remove_duplicates = self.database.remove_duplicate_devices_from_user("User1")
        self.assertEqual(remove_duplicates, True)

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                    {
                        "username": "User1",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": [{
                            "prod_id": 123,
                            "name": "Gyldig",
                            "brand": "Enhet",
                            "category": "Test"
                        }]
                    }, {
                        "username": "User2",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }
                ])
    def test_remove_duplicate_devices_from_user_not_removed(self, mock):
        remove_duplicates = self.database.remove_duplicate_devices_from_user("NonUser")
        self.assertEqual(remove_duplicates, False)


    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tests for create_new_device()
    
    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tests for delete_device_from_user()
    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                    {
                        "username": "User1",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": [{
                            "prod_id": 123,
                            "name": "Gyldig",
                            "brand": "Enhet",
                            "category": "Test"
                        }]
                    }, {
                        "username": "User2",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }
                ])
    def test_delete_device_from_user_deleted(self, mock):
        device = Device.Device(123, "Gyldig", "Enhet", "Test")
        delete_device = self.database.delete_device_from_user("User1", device)
        self.assertEqual(delete_device, True)

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                    {
                        "username": "User1",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": [{
                            "prod_id": 123,
                            "name": "Gyldig",
                            "brand": "Enhet",
                            "category": "Test"
                        }]
                    }, {
                        "username": "User2",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }
                ])
    def test_delete_device_from_user_user_not_found(self, mock):
        device = device = Device.Device(123, "Gyldig", "Enhet", "Test")
        delete_device = self.database.delete_device_from_user("NonUser", device)
        self.assertEqual(delete_device, False)

    @mock.patch("jsondb.JsonDatabase.read_json", return_value=[
                    {
                        "username": "User1",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": [{
                            "prod_id": 123,
                            "name": "Gyldig",
                            "brand": "Enhet",
                            "category": "Test"
                        }]
                    }, {
                        "username": "User2",
                        "password": "password",
                        "email": "epost@epost.com",
                        "devices": []
                    }
                ])
    def test_delete_device_from_user_device_not_found(self, mock):
        device = Device.Device(69, "Ikke", "En", "Enhet")
        delete_device = self.database.delete_device_from_user("User1", device)
        self.assertEqual(delete_device, "Device could not be found")

    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tests for modify_device_information()

    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tests for get_current_user()

    # -------------------------------------------------------------------------------------------
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -------------------------------------------------------------------------------------------
    # Tests for add_device_to_current_user()

    def test_cleanup(self):
        path = os.path.join(os.path.dirname(__file__))
        pathList = path.split("\\")
        pathList.pop()
        pathList.append("test.json")
        path = "\\".join(pathList)
        print(path)
        
        if os.path.exists(path):
            os.remove(path)
        
        
if __name__ == '__main__':
    unittest.main()
    


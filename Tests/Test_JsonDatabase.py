import unittest
from unittest import mock, TestCase
import sys
import os


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(project_root)

from jsondb import JsonDatabase

class TestJsonDatabase(unittest.TestCase):
    def setUp(self):
        self.database = JsonDatabase("test")

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
    def test_add_user_to_json(self):
        pass

    # -------------------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()


import unittest
from unittest import mock, TestCase
import sys
import os

sys.path.append('../')

from jsondb import JsonDatabase

class TestJsonDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self.database = JsonDatabase("test")

    @mock.patch(JsonDatabase.read_json(), return_value=[
            {
                "name": "TakenName",
                "password": "p",
                "email": "1@2.3",
                "devices": []
            }
        ])
    def test_is_username_taken_true(self):
        self.assertEqual(self.database.is_username_taken("TakenName"), True)



    def test_add_user_to_json(self):
        self.add_user_to_json("Test1", "Passord123", "ma!i?l@mail.com")
        self.add_user_to_json("Test2", "Pa123", "mail.m@mail.com")
        self.add_user_to_json("Test3", "Passord123", "mail")




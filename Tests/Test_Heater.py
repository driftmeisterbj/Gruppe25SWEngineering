import unittest
from unittest.mock import patch
import sys

sys.path.append('../')
sys.path.append('Devices/')
from Heater import Heater

class TestHeater(unittest.TestCase):

    def setUp(self):
        self.heater = Heater(45, "60T", "Siemens")

    def test_initial_temperature(self):
        self.assertEqual(self.heater.temperature, 15)

    @patch('builtins.print')
    def test_turn_on_off_heater(self,mock_print):
        self.heater.turn_on_device()
        mock_print.assert_called_with('Siemens 60T has been turned on.')
        self.assertTrue(self.heater.on)
        self.heater.turn_off_device()
        mock_print.assert_called_with('Siemens 60T has been turned off.')
        self.assertFalse(self.heater.on)

    @patch('builtins.print')
    def test_set_temperature_valid(self,mock_print):
        self.heater.set_temperature(25)
        self.assertEqual(self.heater.temperature, 25)
        mock_print.assesrt_called_with('Siemens 60T is now set to 25 Celcius.')

    @patch('builtins.print')
    def test_set_temperature_invalid(self, mock_print):
        self.heater.set_temperature(10)
        self.assertEqual(self.heater.temperature, 15)
        mock_print.assert_called_with('Invalid temperature, must be between 15 and 30 degrees.')

    def test_set_temperature_non_integer(self):
        with self.assertRaises(ValueError):
            self.heater.set_temperature("abc")
        self.assertEqual(self.heater.temperature, 15)

    @patch('builtins.print')
    def test_status_on(self,mock_print):
        self.heater.turn_on_device()
        mock_print.assert_called_with('Siemens 60T has been turned on.')
        status = self.heater.status()
        self.assertEqual(status, "Siemens 60T is on, temperature: 15 celsius.")

    def test_status_off(self):
        #self.heater.turn_off_device()
        status = self.heater.status()
        self.assertEqual(status, "Siemens 60T is off.")

if __name__ == '__main__':
    unittest.main()

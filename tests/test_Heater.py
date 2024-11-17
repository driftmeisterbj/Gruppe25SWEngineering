import unittest
from unittest.mock import patch
import sys

sys.path.append('../')
sys.path.append('devices/')
from heater import Heater

class TestHeater(unittest.TestCase):

    def setUp(self):
        self.heater = Heater(1, "60T", "Siemens")

    def test_initial_temperaturee(self):
        self.assertEqual(self.heater.prod_id, 1)
        self.assertEqual(self.heater.name, '60T')
        self.assertEqual(self.heater.brand, 'Siemens')
        self.assertEqual(self.heater.category, 'Heater')
        self.assertEqual(self.heater.temperature, 15)

    def test_turn_on_off_heater(self):
        self.heater.on = False
        self.assertFalse(self.heater.on)
        self.heater.turn_on_device()
        self.assertTrue(self.heater.on)

        self.heater.on = True
        self.assertTrue(self.heater.on)
        self.heater.turn_off_device()
        self.assertFalse(self.heater.on)

    def test_set_temperature_valid(self):
        self.assertEqual(self.heater.temperature,15)
        self.heater.set_temperature('+')
        self.assertEqual(self.heater.temperature,16)

        self.heater.temperature = 20
        self.assertEqual(self.heater.temperature,20)
        self.heater.set_temperature('-')
        self.assertEqual(self.heater.temperature, 19)


    def test_set_temperature_above_below_limit(self):
        self.heater.temperature = 15
        self.assertEqual(self.heater.temperature,15)
        self.heater.set_temperature('-')
        self.assertEqual(self.heater.temperature,15)

        self.heater.temperature = 30
        self.assertEqual(self.heater.temperature,30)
        self.heater.set_temperature('+')
        self.assertEqual(self.heater.temperature,30)

if __name__ == '__main__':
    unittest.main()

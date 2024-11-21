import unittest
from unittest.mock import patch
import sys

sys.path.append('../')
sys.path.append('devices/')
from fridge import Fridge

class TestFridge(unittest.TestCase):
    
    def setUp(self):
        self.fridge = Fridge(1,"M1","Miele")

    def test_initial_temperaturee(self):
        self.assertEqual(self.fridge.prod_id, 1)
        self.assertEqual(self.fridge.name, 'M1')
        self.assertEqual(self.fridge.brand, 'Miele')
        self.assertEqual(self.fridge.category, 'Fridge')
        self.assertEqual(self.fridge.temperature, 4)

    def test_turn_on_off_fridge(self):
        self.fridge.on = False
        self.assertFalse(self.fridge.on)
        self.fridge.turn_on_device()
        self.assertTrue(self.fridge.on)

        self.fridge.on = True
        self.assertTrue(self.fridge.on)
        self.fridge.turn_off_device()
        self.assertFalse(self.fridge.on)

    def test_set_temperature_valid(self):
        self.assertEqual(self.fridge.temperature,4)
        self.fridge.set_temperature('+')
        self.assertEqual(self.fridge.temperature,5)

        self.fridge.temperature = 4
        self.assertEqual(self.fridge.temperature,4)
        self.fridge.set_temperature('-')
        self.assertEqual(self.fridge.temperature, 3)


    def test_set_temperature_above_below_limit(self):
        self.fridge.temperature = 2
        self.assertEqual(self.fridge.temperature,2)
        self.fridge.set_temperature('-')
        self.assertEqual(self.fridge.temperature,2)

        self.fridge.temperature = 12
        self.assertEqual(self.fridge.temperature,12)
        self.fridge.set_temperature('+')
        self.assertEqual(self.fridge.temperature,12)


if __name__ == '__main__':
    unittest.main()

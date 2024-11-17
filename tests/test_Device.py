import unittest
from unittest.mock import patch
import sys

sys.path.append('../')
sys.path.append('devices/')
from Device import Device

class TestDevice(unittest.TestCase):

    def setUp(self):
        self.device = Device(1, "ExampleName", "ExampleBrand",'ExampleCategory')

    def test_initial_temperaturee(self):
        self.assertEqual(self.device.prod_id, 1)
        self.assertEqual(self.device.name, 'ExampleName')
        self.assertEqual(self.device.brand, 'ExampleBrand')
        self.assertEqual(self.device.category, 'ExampleCategory')
        self.assertFalse(self.device.on)

    def test_turn_on_off_device(self):
        self.device.on = False
        self.assertFalse(self.device.on)
        self.device.turn_on_device()
        self.assertTrue(self.device.on)

        self.device.on = True
        self.assertTrue(self.device.on)
        self.device.turn_off_device()
        self.assertFalse(self.device.on)


if __name__ == '__main__':
    unittest.main()

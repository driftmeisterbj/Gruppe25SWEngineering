import unittest
from unittest.mock import patch
import sys
sys.path.append('../')
sys.path.append('Devices/')
from Light import Light

class TestLight(unittest.TestCase):

    def setUp(self):
        self.light = Light(1, "Desk Lamp", "Philips")

    def test_initial_values(self):
        self.assertEqual(self.light.prod_id, 1)
        self.assertEqual(self.light.name, "Desk Lamp")
        self.assertEqual(self.light.brand, "Philips")
        self.assertEqual(self.light.category, 'Light')
        self.assertEqual(self.light.brightness, 5)
        self.assertFalse(self.light.on)

    def test_set_brightness_valid(self):
        self.light.set_brightness('+')
        self.assertEqual(self.light.brightness, 6)
        self.light.set_brightness('-')
        self.assertEqual(self.light.brightness, 5)


    def test_set_brightness_above_and_below_limit(self):
        self.light.brightness = 10
        self.assertEqual(self.light.brightness,10)
        self.light.set_brightness('+')
        self.assertEqual(self.light.brightness,10)

        self.light.brightness = 0
        self.assertEqual(self.light.brightness,0)
        self.light.set_brightness('-')
        self.assertEqual(self.light.brightness, 0)
        

    def test_turn_on_off_light(self):
        self.light.on = False
        self.assertFalse(self.light.on)
        self.light.turn_on_device()
        self.assertTrue(self.light.on)

        self.light.on = True
        self.assertTrue(self.light.on)
        self.light.turn_off_device()
        self.assertFalse(self.light.on)




if __name__ == '__main__':
    unittest.main()

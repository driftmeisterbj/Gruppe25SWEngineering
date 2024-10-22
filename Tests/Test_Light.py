import unittest
from unittest.mock import patch
from Light import Light

class TestLight(unittest.TestCase):

    def setUp(self):
        self.light = Light("001", "Desk Lamp", "Philips", 5)

    def test_initial_values(self):
        # Testing that initial values are set correctly
        self.assertEqual(self.light.name, "Desk Lamp")
        self.assertEqual(self.light.brand, "Philips")
        self.assertEqual(self.light.brightness, 5)
        self.assertFalse(self.light.on)

    def test_set_brightness_valid(self):
        # Testing set_brightness with valid values
        with patch('builtins.print') as mocked_print:
            self.light.set_brightness(7)
            mocked_print.assert_called_with("Philips Desk Lamp brightness set to: 7")
            self.assertEqual(self.light.brightness, 7)
    def test_set_brightness_to_zero(self):
        # Testing setting brightness below 1
        with patch('builtins.print') as mocked_print:
            self.light.set_brightness(-1)
            mocked_print.assert_called_with("Philips Desk Lamp brightness set to: 0")
            self.assertEqual(self.light.brightness, 0)

    def test_set_brightness_above_max(self):
        # Testing setting brightness above 10
        with patch('builtins.print') as mocked_print:
            self.light.set_brightness(11)
            mocked_print.assert_called_with("Philips Desk Lamp brightness set to: 10")
            self.assertEqual(self.light.brightness, 10)

    def test_set_brightness_invalid_input(self):
        # Testing set_brightness with non-integer values
        with patch('builtins.print') as mocked_print:
            self.light.set_brightness("abc")
            mocked_print.assert_called_with("Brightness must be number")
            self.assertEqual(self.light.brightness, 5)  # Brightness remains unchanged

    def test_status_when_on(self):
        # Testing status display when the light is on
        self.light.on = True
        with patch('builtins.print') as mocked_print:
            self.light.status()
            mocked_print.assert_called_with("Philips Desk Lamp is turned on, brightness: 5")

    def test_status_when_off(self):
        # Testing status display when the light is off
        with patch('builtins.print') as mocked_print:
            self.light.status()
            mocked_print.assert_called_with("Philips Desk Lamp is off.")

if __name__ == '__main__':
    unittest.main()

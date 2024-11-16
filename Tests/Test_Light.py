import unittest
from unittest.mock import patch
import sys
sys.path.append('../')
sys.path.append('Devices/')
from Light import Light

#--------- Tests being done ---------#

# setUp: Sets up a Light object for each test method

#1. test_initial_values: Checks initial attributes of a newly instantiated Light object
#2. test_set_brightness_valid: Verifies that the brightness can be set to a valid value within the expected range
#3. test_set_brightness_below_zero: Tests that setting brightness below the minimum threshold sets it to zero
#4. test_set_brightness_above_max: Ensures that setting brightness above the maximum limit sets it to the maximum
#5. test_set_brightness_invalid_input: Confirms handling of non-integer inputs for brightness
#6. test_status_when_on: Tests the output message when the light is turned on
#7. test_status_when_off: Tests the output message when the light is turned off
#8. test_category_being_set_correctly: Checks that the category attribute is correctly set to 'Light'
#9. test_turn_on_off_light: Checks that the turn on and off functions from parent class work correctly

#------------------------------------------------------------------------------------#

class TestLight(unittest.TestCase):

    def setUp(self):
        self.light = Light(1, "Desk Lamp", "Philips")

    def test_initial_values(self):
        # Testing that initial values are set correctly
        self.assertEqual(self.light.prod_id, 1)
        self.assertEqual(self.light.name, "Desk Lamp")
        self.assertEqual(self.light.brand, "Philips")
        self.assertEqual(self.light.category, 'Light')
        self.assertEqual(self.light.brightness, 5)
        self.assertFalse(self.light.on)

    def test_set_brightness_valid(self):
        # Testing set_brightness with valid values
        with patch('builtins.print') as mocked_print:
            self.light.set_brightness('+')
            self.assertEqual(self.light.brightness, 6)


    def test_set_brightness_invalid_input(self):
        pass

    def test_turn_on_off_light(self):
        pass

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
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
#9. test_turn_on_off_light: Checks that the turn on and off functions from parent class works correctly

#------------------------------------------------------------------------------------#




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
    def test_set_brightness_below_zero(self):
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

    def test_category_being_set_Correctly(self):
        self.assertEqual(self.light.category,'Light')


    def test_turn_on_off_light(self):
        #Light is initially off check
        self.assertFalse(self.light.on)
        #Turns on light
        self.light.turn_on_device()
        #Light should then be on check
        self.assertTrue(self.light.on)
        #Turns off light
        self.light.turn_off_device()
        #Checks that light is now off
        self.assertFalse(self.light.on)



if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
import sys

sys.path.append('../')
sys.path.append('Devices/')
from Fridge import Fridge


#--------- Tests being done ---------#

# setUp: Sets up a Fridge object for each test method.

#1. test_initial_temperature: Verifies that the fridge initializes with a default temperature of 4 degrees Celsius.
#2. test_turn_on_off_fridge: Checks that the fridge turns on and off correctly, with corresponding print statements confirming each action.
#3. test_set_temperature_valid: Confirms that setting the temperature within a valid range (e.g., 6) updates the fridge temperature and triggers the correct print message.
#4. test_set_temperature_invalid: Ensures that setting an invalid temperature (e.g., 15) triggers an error message without changing the fridge temperature.
#5. test_set_temperature_non_integer: Verifies that attempting to set a non-integer temperature (e.g., "abc") raises a ValueError, leaving the temperature unchanged.
#6. test_status_on: Checks that the fridge’s status correctly displays as "on" when powered on, including the current temperature.
#7. test_status_off: Confirms that the fridge’s status correctly displays as "off" when powered off.

#------------------------------------------------------------------------------------#



class TestSmartKjøleskap(unittest.TestCase):
    
    def setUp(self):
        self.fridge = Fridge("456","M1","Miele")

    def test_initial_temperaturee(self):
        self.assertEqual(self.fridge.temperature, 4)

    @patch('builtins.print')
    def test_turn_on_off_fridge(self, mock_print):
        self.fridge.turn_on_device()
        self.assertTrue(self.fridge.on)
        mock_print.assert_called_with("Miele M1 has been turned on.")
        self.fridge.turn_off_device()
        self.assertFalse(self.fridge.on)
        mock_print.assert_called_with("Miele M1 has been turned off.")

    @patch('builtins.print')
    def test_set_temperature_valid(self,mock_print):
        self.fridge.set_temperature(6)
        mock_print.assert_called_with("Miele M1 is now set to 6 Celcius")
        self.assertEqual(self.fridge.temperature, 6)
    @patch('builtins.print')
    def test_set_temperature_invalid(self,mock_print):
        self.fridge.set_temperature(15)
        mock_print.assert_called_with("Invalid temperature, must be between 2 and 12 degrees")
        self.assertEqual(self.fridge.temperature, 4)

    def test_set_temperature_non_integer(self):
        with self.assertRaises(ValueError):
            self.fridge.set_temperature("abc")
        self.assertEqual(self.fridge.temperature, 4)

    @patch('builtins.print')
    def test_status_on(self, mock_print):
        self.fridge.turn_on_device()
        #Vet ikke om denne linjen trengs, siden vi har testet det i turn_on_off testen
        #Har den der i tilfelle folk tror det er lurt
        mock_print.assert_called_with("Miele M1 has been turned on.")

        status = self.fridge.status()
        self.assertEqual(status, "Miele M1 is on. Current temperature: 4 Celcius")

    def test_status_off(self):
        status = self.fridge.status()
        self.assertEqual(status, "Miele M1 is off")

if __name__ == '__main__':
    unittest.main()

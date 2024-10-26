import unittest
import sys

sys.path.append('../')
sys.path.append('Devices/')
from smart_kjoleskap import SmartKjøleskap

class TestSmartKjøleskap(unittest.TestCase):
    
    def setUp(self):
        self.kjoleskap = SmartKjøleskap("TestKjøleskap", "TestID", "Brand", "Category")

    def test_initial_temperature(self):
        self.assertEqual(self.kjoleskap.temperatur, 4)

    def test_skru_på(self):
        self.kjoleskap.turn_on_device()
        self.assertTrue(self.kjoleskap.on)

    def test_skru_av(self):
        self.kjoleskap.turn_on_device()
        self.kjoleskap.turn_off_device()
        self.assertFalse(self.kjoleskap.on)

    def test_sett_temperatur_valid(self):
        self.kjoleskap.sett_temperatur(6)
        self.assertEqual(self.kjoleskap.temperatur, 6)

    def test_sett_temperatur_invalid(self):
        self.kjoleskap.sett_temperatur(15)
        self.assertEqual(self.kjoleskap.temperatur, 4)

    def test_sett_temperatur_non_integer(self):
        self.kjoleskap.sett_temperatur("abc")
        self.assertEqual(self.kjoleskap.temperatur, 4)

    def test_status_på(self):
        self.kjoleskap.turn_on_device()
        self.assertEqual(self.kjoleskap.status(), "TestKjøleskap (Brand) er på, temperatur: 4 grader.")

    def test_status_av(self):
        self.kjoleskap.turn_off_device()
        self.assertEqual(self.kjoleskap.status(), "TestKjøleskap (Brand) er av.")

if __name__ == '__main__':
    unittest.main()

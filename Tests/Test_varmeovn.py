import unittest
import sys

sys.path.append('../')
sys.path.append('Devices/')
from smart_varmeovn import SmartVarmeovn

class TestSmartVarmeovn(unittest.TestCase):

    def setUp(self):
        self.varmeovn = SmartVarmeovn("TestVarmeovn", "TestID", "Brand", "Varmeovn")

    def test_initial_temperature(self):
        self.assertEqual(self.varmeovn.temperatur, 20)

    def test_skru_på(self):
        self.varmeovn.turn_on_device()
        self.assertTrue(self.varmeovn.on)

    def test_skru_av(self):
        self.varmeovn.turn_on_device()
        self.varmeovn.turn_off_device()
        self.assertFalse(self.varmeovn.on)

    def test_sett_temperatur_valid(self):
        self.varmeovn.sett_temperatur(25)
        self.assertEqual(self.varmeovn.temperatur, 25)

    def test_sett_temperatur_invalid(self):
        self.varmeovn.sett_temperatur(10)
        self.assertEqual(self.varmeovn.temperatur, 20)

    def test_sett_temperatur_non_integer(self):
        self.varmeovn.sett_temperatur("abc")
        self.assertEqual(self.varmeovn.temperatur, 20)

    def test_status_på(self):
        self.varmeovn.turn_on_device()
        self.assertEqual(self.varmeovn.status(), "TestVarmeovn (Brand) er på, temperatur: 20 grader.")

    def test_status_av(self):
        self.varmeovn.turn_off_device()
        self.assertEqual(self.varmeovn.status(), "TestVarmeovn (Brand) er av.")

if __name__ == '__main__':
    unittest.main()

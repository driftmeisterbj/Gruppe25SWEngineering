import unittest
from smart_varmeovn import SmartVarmeovn

class TestSmartVarmeovn(unittest.TestCase):
    
    def setUp(self):
        self.ovnen = SmartVarmeovn("TestVarmeovn")

    def test_initial_temperature(self):
        self.assertEqual(self.ovnen.temperatur, 20)

    def test_skru_på(self):
        self.ovnen.skru_på()
        self.assertTrue(self.ovnen.på)

    def test_skru_av(self):
        self.ovnen.skru_på()
        self.ovnen.skru_av()
        self.assertFalse(self.ovnen.på)

    def test_sett_temperatur_valid(self):
        self.ovnen.sett_temperatur(25)
        self.assertEqual(self.ovnen.temperatur, 25)

    def test_sett_temperatur_invalid(self):
        with self.assertRaises(SystemExit):
            self.ovnen.sett_temperatur(10)
        self.assertEqual(self.ovnen.temperatur, 20)

    def test_sett_temperatur_non_integer(self):
        with self.assertRaises(SystemExit):
            self.ovnen.sett_temperatur("abc")
        self.assertEqual(self.ovnen.temperatur, 20)

    def test_status_på(self):
        self.ovnen.skru_på()
        self.assertEqual(self.ovnen.status(), "TestVarmeovn er på, temperatur: 20 grader.")

    def test_status_av(self):
        self.ovnen.skru_av()
        self.assertEqual(self.ovnen.status(), "TestVarmeovn er av.")

if __name__ == '__main__':
    unittest.main()

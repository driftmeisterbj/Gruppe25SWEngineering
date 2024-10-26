import unittest
from smart_kjoleskap import SmartKjøleskap

class TestSmartKjøleskap(unittest.TestCase):
    
    def setUp(self):
        self.kjoleskap = SmartKjøleskap("TestKjøleskap")

    def test_initial_temperature(self):
        self.assertEqual(self.kjoleskap.temperatur, 4)

    def test_skru_på(self):
        self.kjoleskap.skru_på()
        self.assertTrue(self.kjoleskap.på)

    def test_skru_av(self):
        self.kjoleskap.skru_på()
        self.kjoleskap.skru_av()
        self.assertFalse(self.kjoleskap.på)

    def test_sett_temperatur_valid(self):
        self.kjoleskap.sett_temperatur(6)
        self.assertEqual(self.kjoleskap.temperatur, 6)

    def test_sett_temperatur_invalid(self):
        with self.assertRaises(SystemExit):
            self.kjoleskap.sett_temperatur(15)
        self.assertEqual(self.kjoleskap.temperatur, 4)

    def test_sett_temperatur_non_integer(self):
        with self.assertRaises(SystemExit):
            self.kjoleskap.sett_temperatur("abc")
        self.assertEqual(self.kjoleskap.temperatur, 4)

    def test_status_på(self):
        self.kjoleskap.skru_på()
        self.assertEqual(self.kjoleskap.status(), "TestKjøleskap er på, temperatur: 4 grader.")

    def test_status_av(self):
        self.assertEqual(self.kjoleskap.status(), "TestKjøleskap er av.")

if __name__ == '__main__':
    unittest.main()

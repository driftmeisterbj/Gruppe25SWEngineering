import unittest
from unittest.mock import patch
from enhet import Enhet
from smartlys import SmartLys

class TestSmartLys(unittest.TestCase):

    def setUp(self):
        self.smartlys = SmartLys("Stue")

    def test_initial_values(self):
        # Tester at initialverdiene settes korrekt.
        self.assertEqual(self.smartlys.navn, "Stue")
        self.assertEqual(self.smartlys.lysstyrke, 5)
        self.assertFalse(self.smartlys.på)

    def test_sett_lysstyrke_valid(self):
        # Tester at sett_lysstyrke fungerer med gyldige verdier.
        self.smartlys.sett_lysstyrke(7)
        self.assertEqual(self.smartlys.lysstyrke, 7)

    def test_sett_lysstyrke_invalid(self):
        # Tester at sett_lysstyrke håndterer ugyldige verdier.
        with patch('builtins.print') as mocked_print:
            self.smartlys.sett_lysstyrke(15)  # Over gyldig område
            mocked_print.assert_called_with("Ugyldig lysstyrke! Lysstyrken må være mellom 1 og 10.")
            self.assertEqual(self.smartlys.lysstyrke, 5)

    def test_sett_lysstyrke_non_integer(self):
        # Tester at sett_lysstyrke håndterer ugyldige ikke-heltall.
        with patch('builtins.print') as mocked_print:
            self.smartlys.sett_lysstyrke("abc")
            mocked_print.assert_called_with("Vennligst skriv inn en gyldig heltallverdi for lysstyrken.")
            self.assertEqual(self.smartlys.lysstyrke, 5)

    def test_status_when_on(self):
        # Tester at statusen vises korrekt når lyset er på.
        self.smartlys.på = True
        with patch('builtins.print') as mocked_print:
            self.smartlys.status()
            mocked_print.assert_called_with("Stue er på, lysstyrke: 5.")

    def test_status_when_off(self):
        # Tester at statusen vises korrekt når lyset er av.
        with patch('builtins.print') as mocked_print:
            self.smartlys.status()
            mocked_print.assert_called_with("Stue er av.")

if __name__ == '__main__':
    unittest.main()

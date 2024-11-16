import unittest
from unittest.mock import patch
import sys

sys.path.append('../')
sys.path.append('Devices/')
from Device import Device

class TestDevice(unittest.TestCase):

    def setUp(self):
        self.device = Device("1", "RoboCleaner", "Miele", "Vacuum Cleaner")

    def test_turn_on_device(self, mock_print):
        self.device.turn_on_device()
        self.assertTrue(self.device.on)
        mock_print.assert_called_with("Miele RoboCleaner has been turned on.")

    def test_turn_off_device(self, mock_print):
        self.device.turn_off_device()
        self.assertTrue(self.device.off)
        mock_print.assert_called_with("Miele RoboCleaner has been turned off.")

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
from Lock import SmartLock

class TestSmartLock(unittest.TestCase):
    
    def setUp(self):
        self.smart_lock = SmartLock("001", "Front Door", "Yale")

    def test_initial_status(self):
        self.assertEqual(self.smart_lock.status, "Unlocked")
        self.assertEqual(self.smart_lock.entry_code, "0727")

    @patch('builtins.print')
    def test_set_entry_code_valid(self, mock_print):
        self.smart_lock.set_entry_code("1234")
        self.assertEqual(self.smart_lock.entry_code, "1234")
        mock_print.assert_called_with("Entry code has been updated to: 1234")

    @patch('builtins.print')
    def test_set_entry_code_invalid(self, mock_print):
        self.smart_lock.set_entry_code("abcd")
        mock_print.assert_called_with("Invalid entry code Must be a 4-digit number")
        self.assertEqual(self.smart_lock.entry_code, "0727")

    @patch('builtins.print')
    def test_lock(self, mock_print):
        self.smart_lock.lock()
        self.assertEqual(self.smart_lock.status, "Locked")
        mock_print.assert_called_with("Yale Front Door is now locked")
    
    @patch('builtins.print')
    def test_unlock_successful(self, mock_print):
        self.smart_lock.lock()
        self.smart_lock.unlock("0727")
        self.assertEqual(self.smart_lock.status, "Unlocked")
        mock_print.assert_called_with("Yale Front Door is now unlocked")

    @patch('builtins.print')
    def test_unlock_unsuccessful(self, mock_print):
        self.smart_lock.lock()
        self.smart_lock.unlock("wrongcode")
        self.assertEqual(self.smart_lock.status, "Locked")
        mock_print.assert_called_with("Incorrect entry code. The lock remains locked")

if __name__ == '__main__':
    unittest.main()

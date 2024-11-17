import unittest
from unittest.mock import patch
import sys
sys.path.append('../')
sys.path.append('Devices/')
from Lock import Lock

class TestLock(unittest.TestCase):
    
    def setUp(self):
        self.lock = Lock(1, "Front Door", "Yale")

    def test_initial_status(self):
        self.assertEqual(self.lock.prod_id, 1)
        self.assertEqual(self.lock.name, 'Front Door')
        self.assertEqual(self.lock.brand, 'Yale')
        self.assertEqual(self.lock.category, 'Lock')
        self.assertEqual(self.lock.status, "Unlocked")
        self.assertEqual(self.lock.entry_code, "0727")

    def test_turn_on_off_lock(self):
        self.lock.on = False
        self.assertFalse(self.lock.on)
        self.lock.turn_on_device()
        self.assertTrue(self.lock.on)

        self.lock.on = True
        self.assertTrue(self.lock.on)
        self.lock.turn_off_device()
        self.assertFalse(self.lock.on)

    def test_set_entry_code_valid(self):
        self.assertEqual(self.lock.entry_code,'0727')
        self.lock.set_entry_code('1234')
        self.assertEqual(self.lock.entry_code,'1234')

    def test_set_entry_code_invalid(self):
        self.assertEqual(self.lock.entry_code,'0727')
        self.lock.set_entry_code('abcd')
        self.assertEqual(self.lock.entry_code,'0727')
        self.lock.set_entry_code('12345')
        self.assertEqual(self.lock.entry_code,'0727')

    def test_lock_unlock(self):
        self.assertEqual(self.lock.status,'Unlocked')
        self.assertTrue(self.lock.lock)
        self.lock.lock()
        self.assertEqual(self.lock.status,'Locked')

        self.assertTrue(self.lock.unlock('0727'))
        self.lock.unlock('0727')
        self.assertEqual(self.lock.status,'Unlocked')

    def test_unlock_invalid(self):
        self.lock.status = 'Locked'
        self.assertEqual(self.lock.status,'Locked')
        self.assertFalse(self.lock.unlock('4651'))
        self.lock.unlock('4651')
        self.assertEqual(self.lock.status, 'Locked')
    



if __name__ == '__main__':
    unittest.main()

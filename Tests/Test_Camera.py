import unittest
from unittest.mock import patch

import sys
sys.path.append('../')
sys.path.append('Devices/')
from Camera import Camera

class TestCamera(unittest.TestCase):

    def setUp(self):
        self.camera = Camera(1, "Home Camera", "Nest")

    def test_initial_temperaturee(self):
        self.assertEqual(self.camera.prod_id, 1)
        self.assertEqual(self.camera.name, 'Home Camera')
        self.assertEqual(self.camera.brand, 'Nest')
        self.assertEqual(self.camera.category, 'Camera')
        self.assertFalse(self.camera.on)

    def test_turn_on_off_camera(self):
        self.camera.on = False
        self.assertFalse(self.camera.on)
        self.camera.turn_on_device()
        self.assertTrue(self.camera.on)

        self.camera.on = True
        self.assertTrue(self.camera.on)
        self.camera.turn_off_device()
        self.assertFalse(self.camera.on)

if __name__ == '__main__':
    unittest.main()

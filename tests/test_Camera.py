import unittest
from unittest.mock import patch

import sys
sys.path.append('../')
sys.path.append('devices/')
from camera import Camera

class TestCamera(unittest.TestCase):

    def setUp(self):
        self.camera = Camera(1, "Home Camera", "Nest")

    def test_initial_temperaturee(self):
        self.assertEqual(self.camera.prod_id, 1)
        self.assertEqual(self.camera.name, 'Home Camera')
        self.assertEqual(self.camera.brand, 'Nest')
        self.assertEqual(self.camera.category, 'Camera')
        self.assertFalse(self.camera.on)
        self.assertEqual(self.camera.resolution, '1080p')
        self.assertEqual(self.camera.status, 'Inactive')
        self.assertFalse(self.camera.motion_detection)


    def test_turn_on_off_camera(self):
        self.camera.on = False
        self.assertFalse(self.camera.on)
        self.camera.turn_on_device()
        self.assertTrue(self.camera.on)

        self.camera.on = True
        self.assertTrue(self.camera.on)
        self.camera.turn_off_device()
        self.assertFalse(self.camera.on)

    def test_set_resolution_valid(self):
        self.assertEqual(self.camera.resolution, '1080p')
        self.camera.set_resolution('+')
        self.assertEqual(self.camera.resolution,'1440p')

        self.camera.resolution = '1080p'
        self.assertEqual(self.camera.resolution, '1080p')
        self.camera.set_resolution('-')
        self.assertEqual(self.camera.resolution,'720p')

    def test_set_resolution_above_below_limit(self):
        self.camera.resolution = '4K'
        self.assertEqual(self.camera.resolution,'4K')
        self.camera.set_resolution('+')
        self.assertEqual(self.camera.resolution,'4K')

        self.camera.resolution = '180p'
        self.assertEqual(self.camera.resolution,'180p')
        self.camera.set_resolution('-')
        self.assertEqual(self.camera.resolution,'180p')

    def test_activate(self):
        pass

    def test_deactivate(self):
        self.assertEqual(self.camera.status,'Inactive')
        self.camera.activate()
        self.assertEqual(self.camera.status,'Active')

    def toggle_motion_detection(self):
        self.camera.status = 'Active'
        self.assertEqual(self.camera.status,'Active')
        self.camera.deactivate()
        self.assertEqual(self.camera.status,'Inactive')



if __name__ == '__main__':
    unittest.main()
    

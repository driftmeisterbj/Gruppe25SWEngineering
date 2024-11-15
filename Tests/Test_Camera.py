import unittest
from unittest.mock import patch
from Device import Device
from smart_camera import SmartCamera

class TestSmartCamera(unittest.TestCase):

    def setUp(self):
        self.smart_camera = SmartCamera("002", "Living Room Camera", "Nest")

    def test_initial_status(self):
        self.assertEqual(self.smart_camera.status, "Inactive")
        self.assertEqual(self.smart_camera.resolution, "1080p")
        self.assertFalse(self.smart_camera.motion_detection)

    @patch('builtins.print')
    def test_set_resolution_valid(self, mock_print):
        self.smart_camera.set_resolution("4K")
        self.assertEqual(self.smart_camera.resolution, "4K")
        mock_print.assert_called_with("Resolution has been updated to: 4K")

    @patch('builtins.print')
    def test_set_resolution_invalid(self, mock_print):
        self.smart_camera.set_resolution("8K")
        mock_print.assert_called_with("Invalid resolution. Choose from: 720p, 1080p, or 4K.")
        self.assertEqual(self.smart_camera.resolution, "1080p")

    @patch('builtins.print')
    def test_activate(self, mock_print):
        self.smart_camera.activate()
        self.assertEqual(self.smart_camera.status, "Active")
        mock_print.assert_called_with("Nest Living Room Camera is now active.")

    @patch('builtins.print')
    def test_deactivate(self, mock_print):
        self.smart_camera.deactivate()
        self.assertEqual(self.smart_camera.status, "Inactive")
        mock_print.assert_called_with("Nest Living Room Camera is now inactive.")

    @patch('builtins.print')
    def test_toggle_motion_detection(self, mock_print):
        self.smart_camera.toggle_motion_detection()
        self.assertTrue(self.smart_camera.motion_detection)
        mock_print.assert_called_with("Motion detection has been enabled.")
        
        self.smart_camera.toggle_motion_detection()
        self.assertFalse(self.smart_camera.motion_detection)
        mock_print.assert_called_with("Motion detection has been disabled.")

if __name__ == '__main__':
    unittest.main()

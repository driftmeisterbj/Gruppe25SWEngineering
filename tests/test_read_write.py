import unittest
from unittest.mock import patch, mock_open
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(project_root)
from jsondb import JsonReadWrite
import json


class TestJsonReadWrite(unittest.TestCase):
    @patch('jsondb.open', mock_open(read_data='{"name":"Test"}'))
    def test_read_file_exists(self):
        result = JsonReadWrite.read('dummy.json')
        self.assertEqual(result, {'name': 'Test'})

    @patch('jsondb.open', side_effect=FileNotFoundError)
    def test_read_file_not_found(self, mock_file):
        result = JsonReadWrite.read('non_existent.json')
        self.assertEqual(result, [])

    @patch('jsondb.open', mock_open(read_data='Invalid JSON'))
    def test_read_invalid_json(self):
        result = JsonReadWrite.read('invalid.json')
        self.assertEqual(result, [])

    @patch('jsondb.open', new_callable=mock_open)
    def test_write_successful(self, mock_file):
        data = {"key": "value"}
        with patch('json.dump') as mock_json_dump:
            result = JsonReadWrite.write('dummy.json', data)
            self.assertTrue(result)
            # Capture the actual file handle and assert json.dump calls it
            file_handle = mock_file()
            mock_json_dump.assert_called_once_with(data, file_handle, indent=4)

    @patch('jsondb.open', side_effect=PermissionError)
    def test_write_permission_error(self, mock_file):
        data = {"key": "value"}
        result = JsonReadWrite.write('dummy.json', data)
        self.assertFalse(result)

    @patch('jsondb.open', mock_open())
    def test_reset_successful(self):
        with patch('jsondb.open', mock_open()) as mock_file:
            result = JsonReadWrite.reset('dummy.json')
            self.assertTrue(result)
            mock_file().write.assert_called_once_with("{}")

    @patch('jsondb.open', side_effect=PermissionError)
    def test_reset_permission_error(self, mock_file):
        result = JsonReadWrite.reset('dummy.json')
        self.assertFalse(result)

    @patch('jsondb.open', new_callable=mock_open)
    def test_write_empty_data(self, mock_file):
        data = {}
        with patch('json.dump') as mock_json_dump:
            result = JsonReadWrite.write('dummy.json', data)
            self.assertTrue(result)
            mock_json_dump.assert_called_once_with(data, mock_file(), indent=4)
  
    @patch('jsondb.open', mock_open(read_data='{}'))
    def test_read_empty_file(self):
        result = JsonReadWrite.read('empty.json')
        self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main()

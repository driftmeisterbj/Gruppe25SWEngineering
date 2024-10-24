import unittest
from unittest.mock import patch, mock_open
import sys
sys.path.append('../')
from jsondb import ReadWrite

#Test for read and write functions in JSONdb.py

class TestReadWrite(unittest.TestCase):
    def test_read_file_exists(self):
        mock_data = '{"name":"Test"}'
        with patch('builtins.open',mock_open(read_data=mock_data)) as mocked_file:
            reader = ReadWrite()
            result = reader.read('dummy.json')
            mocked_file.assert_called_once_with('dummy.json', 'r')
            self.assertEqual(result, {'name': 'Test'})
            #print(result)



if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch, mock_open

from Temp_Read_write_copy import JsonReadWrite

#import sys
#sys.path.append('../')
#from jsondb import JsonReadWrite

#Test for read and write functions in JSONdb.py

class TestReadWrite(unittest.TestCase):
    @patch('builtins.open', mock_open(read_data='{"name":"Test"}'))
    def test_read_file_exists(self):
        reader = JsonReadWrite()
        result = reader.read('dummy.json')
        self.assertEqual(result, {'name': 'Test'})


if __name__ == '__main__':
    unittest.main()
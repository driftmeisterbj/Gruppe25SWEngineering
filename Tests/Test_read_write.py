import unittest
from unittest.mock import patch, mock_open
import sys
import os
import trace

# Add the parent directory to sys.path so Python can find jsondb.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import from jsondb
from App.jsondb import JsonReadWrite

# Test for read and write functions in JSONdb.py
class TestReadWrite(unittest.TestCase):
    @patch('jsondb.open', mock_open(read_data='{"name":"Test"}'))
    def test_read_file_exists(self):
        result = JsonReadWrite.read('dummy.json')
        self.assertEqual(result, {'name': 'Test'})

if __name__ == '__main__':
    # Create a tracer that will trace only the relevant file
    tracer = trace.Trace(
        trace=True,
        count=False,
        ignoremods=('sys', '_parser', 'os', 'unittest', 'builtins', 're'),  # Ignore these modules
        ignoredirs=[sys.prefix]  # Ignore system-wide libraries
    )

    # Run the test with the trace
    tracer.run('unittest.main()')

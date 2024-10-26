import unittest
from unittest.mock import patch
import sys
import os
from jsondb import JsonDatabase

sys.path.append(os.path.abspath('..'))

class TestJsonDatabase():
    test_database = JsonDatabase()




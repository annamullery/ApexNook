# test_apexnook.py
"""
Tests for ApexNook module.
"""

import unittest
from apexnook import ApexNook

class TestApexNook(unittest.TestCase):
    """Test cases for ApexNook class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ApexNook()
        self.assertIsInstance(instance, ApexNook)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ApexNook()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

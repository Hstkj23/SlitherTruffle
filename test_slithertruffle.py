# test_slithertruffle.py
"""
Tests for SlitherTruffle module.
"""

import unittest
from slithertruffle import SlitherTruffle

class TestSlitherTruffle(unittest.TestCase):
    """Test cases for SlitherTruffle class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SlitherTruffle()
        self.assertIsInstance(instance, SlitherTruffle)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SlitherTruffle()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
